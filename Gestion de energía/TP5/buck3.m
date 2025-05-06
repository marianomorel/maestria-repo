close all;
clear all;

pkg load control;  % Solo necesario en Octave

% --- Parámetros del conversor DC-DC Buck sincrónico ---
L = 150.33e-6;            % Inductancia (H)
Rs = 50e-3 + 250e-3;      % Resistencia serie (Ohm)
C = 208.33e-9;            % Capacitancia (F)
Resr = 30e-3;             % ESR (Ohm)
Vg = 12;                  % Tensión de entrada (V)
R = 6;                    % Resistencia de carga (Ohm)
VM = 1;                   % Amplitud de rampa PWM (V)
Vref = 6;                 % Tensión de referencia (V)
VREG = 6;                 % Tensión regulada de salida (V)
H = Vref / VREG;

% --- Ceros y polos del sistema ---
wesr = 1 / (C * Resr);
w0 = 1 / sqrt(C * L);
Qload = R / sqrt(L / C);
Qloss = sqrt(L / C) / (Resr + Rs);
Q = Qload * Qloss / (Qload + Qloss);

% --- Mostrar datos clave ---
disp("Frecuencia central (w0) [rad/s]:"); disp(w0);
disp("Cero ESR (wesr) [rad/s]:"); disp(wesr);
disp("Factor de calidad Q:"); disp(Q);

% --- Definición de variable simbólica s ---
s = tf('s');

% --- Función de transferencia del conversor Gvd(s) ---
Gvd = (Vg / VM) * (1 + s / wesr) / (1 + (1/Q)*(s/w0) + (s/w0)^2);

% --- Rango de frecuencia ---
fmin = 10;
fmax = 1e9;

% --- Cálculo de Bode de Gvd ---
[mag, phase, w] = bode(Gvd, {2*pi*fmin, 2*pi*fmax});
f = w / (2*pi);

% --- Márgenes de estabilidad de Gvd ---
[Gm, Pm, Wcg, Wcp] = margin(Gvd);
f_cg = Wcg / (2*pi);
f_cp = Wcp / (2*pi);
Gm_dB = 20*log10(Gm);

% --- Gráfico Bode para Gvd(s) ---
figure(1); clf;
subplot(2,1,1);
semilogx(f, 20*log10(squeeze(mag)), 'b', 'LineWidth', 2);
hold on; grid on;
title('Bode Magnitude and Phase de Gvd(s)');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud (dB)');
xlim([fmin, fmax]); ylim([-100, 40]);
if isfinite(f_cg)
  plot(f_cg, 0, 'ro');
  text(f_cg, 5, sprintf('GM = %.2f dB @ %.1f Hz', Gm_dB, f_cg), 'Color', 'red');
end

subplot(2,1,2);
semilogx(f, squeeze(phase), 'b', 'LineWidth', 2);
hold on; grid on;
xlabel('Frecuencia (Hz)');
ylabel('Fase (°)');
xlim([fmin, fmax]); ylim([-180, 0]);
if isfinite(f_cp)
  plot(f_cp, -180+Pm, 'ro');
  text(f_cp, -180+Pm+10, sprintf('PM = %.1f° @ %.1f Hz', Pm, f_cp), 'Color', 'red');
end

% --- Parámetros del controlador ---
phi_m = deg2rad(Pm);  % Margen de fase deseado
Tu0 = (H / VM) * Vg;
f0 = w0 / (2*pi);
f_p2 = 16e6;
f_I = 2.1 * f_cp;

% Cálculo de f_z y f_p1
f_z  = f_cp * sqrt((1 - sin(phi_m)) / (1 + sin(phi_m)));
f_p1 = f_cp * sqrt((1 + sin(phi_m)) / (1 - sin(phi_m)));

% Conversión de frecuencias a rad/s
w_I  = 2 * pi * f_I;
w_z  = 2 * pi * f_z;
w_p1 = 2 * pi * f_p1;
w_p2 = 2 * pi * f_p2;

% Ganancia Gc0
Gc0 = (1 / Tu0) * (f_cp / f0)^2 * sqrt(f_z / f_p1);

% Definición del controlador Gc(s)
Gc = Gc0 * ((1 + w_I/s) * (1 + s/w_z)) / ((1 + s/w_p1) * (1 + s/w_p2));
disp('Gc(s) ='); disp(Gc);

% --- Bode de Gc(s) ---
[mag_Gc, phase_Gc, w_Gc] = bode(Gc, {2*pi*fmin, 2*pi*fmax});
f_Gc = w_Gc / (2*pi);

figure(2);
subplot(2,1,1);
semilogx(f_Gc, 20*log10(squeeze(mag_Gc)), 'r', 'LineWidth', 2);
grid on;
xlabel('Frecuencia (Hz)');
ylabel('Magnitud (dB)');
title('Bode de Gc(s)');
xlim([fmin, fmax]);

subplot(2,1,2);
semilogx(f_Gc, squeeze(phase_Gc), 'r', 'LineWidth', 2);
grid on;
xlabel('Frecuencia (Hz)');
ylabel('Fase (°)');
xlim([fmin, fmax]);

% --- Producto en lazo abierto ---
Gol = Gvd * Gc;

% --- Bode de lazo abierto ---
[mag_Gol, phase_Gol, w_Gol] = bode(Gol, {2*pi*fmin, 2*pi*fmax});
f_Gol = w_Gol / (2*pi);

% --- Márgenes de estabilidad del lazo abierto ---
[Gm_ol, Pm_ol, Wcg_ol, Wcp_ol] = margin(Gol);
f_cg_ol = Wcg_ol / (2*pi);
f_cp_ol = Wcp_ol / (2*pi);
Gm_ol_dB = 20*log10(Gm_ol);

% --- Gráfico Bode de Gol(s) ---
figure(3);
subplot(2,1,1);
semilogx(f_Gol, 20*log10(squeeze(mag_Gol)), 'k', 'LineWidth', 2);
grid on; hold on;
xlabel('Frecuencia (Hz)');
ylabel('Magnitud (dB)');
title('Bode de lazo abierto G_{ol}(s) = G_{vd}(s) * G_c(s)');
xlim([fmin, fmax]);
if isfinite(f_cg_ol)
  plot(f_cg_ol, 0, 'ro');
  text(f_cg_ol, 5, sprintf('GM = %.2f dB @ %.1f Hz', Gm_ol_dB, f_cg_ol), 'Color', 'red');
end

subplot(2,1,2);
semilogx(f_Gol, squeeze(phase_Gol), 'k', 'LineWidth', 2);
grid on; hold on;
xlabel('Frecuencia (Hz)');
ylabel('Fase (°)');
xlim([fmin, fmax]);
if isfinite(f_cp_ol)
  plot(f_cp_ol, -180 + Pm_ol, 'ro');
  text(f_cp_ol, -180 + Pm_ol + 10, sprintf('PM = %.1f° @ %.1f Hz', Pm_ol, f_cp_ol), 'Color', 'red');
end


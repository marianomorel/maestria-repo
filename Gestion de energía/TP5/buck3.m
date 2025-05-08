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
Vref = 1;                 % Tensión de referencia (V)
VREG = 6;                 % Tensión regulada de salida (V)
H = Vref / VREG;

% --- Ceros y polos del sistema ---
wesr = 1 / (C * Resr);
w0 = 1 / sqrt(C * L);
Qload = R / sqrt(L / C);
Qloss = sqrt(L / C) / (Resr + Rs);
Q = Qload * Qloss / (Qload + Qloss);

% --- Definición de variable simbólica s ---
s = tf('s');

% --- Función de transferencia del conversor Gvd(s) ---
Gvd = Vg * (1 + s / wesr) / (1 + (1/Q)*(s/w0) + (s/w0)^2);

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
Tu0 = (H / VM) * Vg;
f0 = w0 / (2*pi);
f_p2 = 16e6;
f_I = 2.1 * f_cp;

% --- Grados a radianes ---
phi_m = deg2rad(Pm);  % Margen de fase deseado

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
Gol = (H/VM) * Gvd * Gc;

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
%if isfinite(f_cg_ol)
  %plot(f_cg_ol, 0, 'ro');
  %text(f_cg_ol, 5, sprintf('GM = %.2f dB @ %.1f Hz', Gm_ol_dB, f_cg_ol), 'Color', 'red');
%end

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

% --- Definir impedancias de salida ---
Z1 = R;
Z2 = 1/(s*C) + Resr;
Z3 = Rs + s*L;
Z_out_ol = 1/(1/Z1 + 1/Z2 + 1/Z3);
Z_out_cl = Z_out_ol / (1 + Gol);

% --- Rango de frecuencia para Bode ---
w_min = 2*pi*fmin;
w_max = 2*pi*fmax;

% --- Calcular Bode de ambas funciones ---
[mag_ol, phase_ol, w] = bode(Z_out_ol, {w_min, w_max});
[mag_cl, phase_cl, ~] = bode(Z_out_cl, w);

f = w / (2*pi);  % Convertir a Hz

% --- Gráficos de Bode ---
figure(4); clf;

% Magnitud
subplot(2,1,1);
semilogx(f, 20*log10(squeeze(mag_ol)), 'b', 'LineWidth', 2);
hold on;
semilogx(f, 20*log10(squeeze(mag_cl)), 'g', 'LineWidth', 2);
grid on;
title('Impedancia de salida Z_{out}(s): Lazo Abierto vs. Cerrado');
ylabel('Magnitud (dB)');
legend('Z_{out\_ol}', 'Z_{out\_cl}');
xlim([fmin, fmax]);
ylim([-60, 20]);

% Fase
subplot(2,1,2);
semilogx(f, squeeze(phase_ol), 'b', 'LineWidth', 2);
hold on;
semilogx(f, squeeze(phase_cl), 'g', 'LineWidth', 2);
grid on;
xlabel('Frecuencia (Hz)');
ylabel('Fase (°)');
legend('Z_{out\_ol}', 'Z_{out\_cl}');
xlim([fmin, fmax]);
ylim([-180, 180]);

disp('Funciones Z_out_ol(s) y Z_out_cl(s) calculadas y graficadas.');

% --- Mostrar todos los parámetros y variables al final ---
disp(' ');
disp('--- Parámetros dados ---');
disp(['L = ', num2str(L), ' H']);
disp(['Rs = ', num2str(Rs), ' Ohm']);
disp(['C = ', num2str(C), ' F']);
disp(['Resr = ', num2str(Resr), ' Ohm']);
disp(['Vg = ', num2str(Vg), ' V']);
disp(['R = ', num2str(R), ' Ohm']);
disp(['VM = ', num2str(VM), ' V']);
disp(['Vref = ', num2str(Vref), ' V']);
disp(['VREG = ', num2str(VREG), ' V']);
disp(['H = ', num2str(H)]);

disp(' ');
disp('--- Variables calculadas ---');
disp(['fesr = ', num2str(wesr/(2*pi)), ' Hz']);
disp(['f0 = ', num2str(w0/(2*pi)), ' Hz']);
disp(['Qload = ', num2str(Qload)]);
disp(['Qloss = ', num2str(Qloss)]);
disp(['Q = ', num2str(Q)]);

disp(' ');
disp('--- Margenes de estabilidad de Gvd(s) ---');
disp(['(Gm) = ', num2str(Gm_dB), ' dB']);
disp(['Frecuencia de GM (f_cg) = ', num2str(f_cg), ' Hz']);
disp(['(Pm) = ', num2str(Pm), ' grados']);
disp(['Frecuencia de PM (f_cp) = ', num2str(f_cp), ' Hz']);

disp(' ');
disp('--- Parámetros del controlador ---');
disp(['Tu0 = ', num2str(Tu0)]);
disp(['f_I = ', num2str(f_I), ' Hz']);
disp(['f_z = ', num2str(f_z), ' Hz']);
disp(['f_p1 = ', num2str(f_p1), ' Hz']);
disp(['f_p2 = ', num2str(f_p2), ' Hz']);
disp(['phi_m = ', num2str(rad2deg(phi_m)), ' grados']);
disp(['Gc0 = ', num2str(Gc0)]);

disp(' ');
disp('--- Margenes de estabilidad del sistema en lazo abierto ---');
disp(['(Pm_T) = ', num2str(Pm_ol), ' grados']);
disp(['Frecuencia PM_T) = ', num2str(f_cp_ol), ' Hz']);


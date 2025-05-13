close all;
clear all;

% Parámetros del conversor DC-DC Buck sincrónico
L = 150.33e-6; % Inductancia (Henrios)
Rs = 50e-3 + 250e-3; % Resistencia serie (Ohmios)
C = 208.33e-9; % Capacitancia (Faradios)
Resr = 30e-3; % Resistencia serie equivalente (Ohmios)
Vg = 12; % Tensión de entrada (Voltios)
R = 6; % Resistencia de carga (Ohmios)
VM = 1; % Amplitud de rampa PWM
Vref = 6; % Tensión de referencia (Voltios)
VREG = 6; % Tensión regulada de salida (Voltios)
H = Vref / VREG;

% Ceros y polos
wesr = 1 / (C * Resr); % Cero de la ESR (rad/s)
wo = 1 / sqrt(C * L); % Frecuencia natural del par complejo
Qload = R / sqrt(L / C);
Qloss = sqrt(L / C) / (Resr + Rs);
Q = Qload * Qloss / (Qload + Qloss);

% Mostrar algunos datos
disp("Frecuencia central (wo) [rad/s]:"); disp(wo);
disp("Cero ESR (wesr) [rad/s]:"); disp(wesr);
disp("Factor de calidad Q:"); disp(Q);

% Definición de función transferencia Gvd(s)
pkg load control;
s = tf('s');
Gvd = (Vg / VM) * (1 + s / wesr) / (1 + (1/Q)*(s/wo) + (s/wo)^2);

% Rango de frecuencia
fmin = 300;
fmax = 1e9;

% Calcular diagrama de Bode
[mag, phase, w] = bode(Gvd, {2*pi*fmin, 2*pi*fmax});
f = w / (2*pi);

% Calcular márgenes de estabilidad
[Gm, Pm, Wcg, Wcp] = margin(Gvd);

% Convertir a unidades más comprensibles
f_cg = Wcg / (2*pi); % Frecuencia cruce de ganancia
f_cp = Wcp / (2*pi); % Frecuencia cruce de fase
Gm_dB = 20*log10(Gm); % Ganancia en dB

% Gráfico Bode con anotaciones
figure(1); clf;

% Magnitud
subplot(2,1,1);
semilogx(f, 20*log10(squeeze(mag)), 'b', 'LineWidth', 2);
hold on;
grid on;
title('Bode Magnitude and Phase');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud (dB)');
xlim([fmin, fmax]);
ylim([-100, 40]);

% Anotar margen de ganancia
if isfinite(f_cg)
  plot(f_cg, 0, 'ro');
  text(f_cg, 5, sprintf('GM = %.2f dB @ %.1f Hz', Gm_dB, f_cg), 'Color', 'red');
end

% Fase
subplot(2,1,2);
semilogx(f, squeeze(phase), 'b', 'LineWidth', 2);
hold on;
grid on;
xlabel('Frecuencia (Hz)');
ylabel('Fase (°)');
xlim([fmin, fmax]);
ylim([-180, 0]);

% Anotar margen de fase
if isfinite(f_cp)
  plot(f_cp, -180+Pm, 'ro');
  text(f_cp, -180+Pm+10, sprintf('PM = %.1f° @ %.1f Hz', Pm, f_cp), 'Color', 'red');
end


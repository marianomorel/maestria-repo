close all;

% Parámetros del conversor DC-DC Buck sincrónico
L = 150.33e-6; % Inductancia (Henrios)
Rs = 50e-3 + 250e-3; % Resistencia serie (RL + Ron) (Ohmios)
C = 208.33e-9; % Capacitancia del filtro de salida (Faradios)
Resr = 30e-3; % Resistencia equivalente serie del capacitor (Ohmios)
Vg = 12; % Tensión de línea (Voltios)
R = 6; % Resistencia de carga (Ohmios)
VM = 1; % Amplitud de la rampa PWM
Vref = 0.8; % Tensión de referencia (Voltios)
VREG = 6; % Tensión de salida regulada (Voltios)
H = Vref / VREG; % Ganancia del realimentador


%% Parámetros de la transferencia Gvd
wesr = 1 / (C * Resr); % Cero de la ESR (rad/s)
wo = 1 / sqrt(C * L); % Frecuencia central del par de polos (rad/s)
Qload = R / sqrt(L / C); % Factor de calidad relacionado con la carga
Qloss = sqrt(L / C) / (Resr + Rs); % Factor de calidad relacionado con las pérdidas
Q = Qload * Qloss / (Qload + Qloss); % Factor de Calidad combinado

% Mostrar los resultados en la consola
disp("Frecuencia central (wo):");
disp(wo);
disp("Cero de la ESR (wesr):");
disp(wesr);
disp("Factor de calidad (Q):");
disp(Q);

%% Transferencia control a la salida a lazo abierto
pkg load control; % Cargar el paquete Control si no está cargado
s = tf('s'); % Definir la variable de Laplace 's'
Gvd = (Vg / VM) * (1 + s / wesr) / (1 + (1 / Q) * (s / wo) + (s / wo)^2);

% Bode de la magnitud y fase
fmin = 300; % Frecuencia mínima = 1000 Hz
fmax = 1e6; % Frecuencia máxima = 1 MHz

% Calcular el diagrama de Bode manualmente
[mag, phase, w] = bode(Gvd); % Obtener magnitud, fase y frecuencia angular
f = w / (2 * pi); % Convertir frecuencia angular a Hz

% Crear gráficos personalizados
figure(1);
clf; % Limpiar la figura actual

% Gráfico de magnitud
subplot(2, 1, 1);
semilogx(f, 20 * log10(squeeze(mag)), 'b', 'LineWidth', 2); % Magnitud en dB
grid on;
title('Synchronous Buck control-to-output responses');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud (dB)');
xlim([fmin, fmax]); % Límites del eje x
ylim([-100, 40]); % Límites del eje y

% Gráfico de fase
subplot(2, 1, 2);
semilogx(f, squeeze(phase), 'b', 'LineWidth', 2); % Fase en grados
grid on;
xlabel('Frecuencia (Hz)');
ylabel('Fase (grados)');
xlim([fmin, fmax]); % Límites del eje x
ylim([-180, 0]); % Límites del eje y

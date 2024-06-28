%L sobremuestreo

% Definimos el eje del tiempo discreto
Fs = 200; % Frecuencia de muestreo (200 Hz)
t = (0:1/Fs:1-1/Fs)'; % Eje de tiempo desde 0 hasta 1 segundo con pasos de 1/Fs

% Definimos un vector de ceros de 200 muestras
x = zeros(length(t), 1);

% Imponemos un '1' en las primeras 20 muestras
x(1:20) = 1;

% Graficamos la señal en un gráfico a la izquierda de una Figura
figure;
subplot(1, 2, 1);
plot(t, x);
title('Señal en el tiempo');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Calculamos la transformada discreta con fft
X = fft(x);

% Ajustamos el eje de frecuencias
N = length(X);
f = (0:N-1)*(Fs/N); % Eje de frecuencias

% Graficamos el módulo del espectro a la derecha de la misma Figura
subplot(1, 2, 2);
plot(f, abs(X));
title('Módulo del Espectro');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');

% Sobremuestreamos y volvemos a graficar igual ajustando el eje del tiempo
Fs_new = 400; % Nueva frecuencia de muestreo (400 Hz)
t_new = (0:1/Fs_new:1-1/Fs_new)'; % Nuevo eje de tiempo desde 0 hasta 1 segundo con pasos de 1/Fs_new

% Definimos un nuevo vector de ceros para el sobremuestreo
x_new = zeros(length(t_new), 1);
x_new(1:40) = 1; % Ajustamos las muestras para 100 ms

% Graficamos la señal sobremuestreada
figure;
subplot(1, 2, 1);
plot(t_new, x_new);
title('Señal Sobremuestreada en el tiempo');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Calculamos la transformada discreta de la señal sobremuestreada
X_new = fft(x_new);

% Ajustamos el eje de frecuencias para la nueva señal
N_new = length(X_new);
f_new = (0:N_new-1)*(Fs_new/N_new); % Nuevo eje de frecuencias

% Graficamos el módulo del espectro de la señal sobremuestreada
subplot(1, 2, 2);
plot(f_new, abs(X_new));
title('Módulo del Espectro Sobremuestreado');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');

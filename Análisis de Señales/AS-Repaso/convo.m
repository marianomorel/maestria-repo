Fs = 100; % Frecuencia de muestreo
t = -4:1/Fs:4; % Tiempo de -4 a 4 con pasos de 1/Fs

% Definir n
n = -2:2;

% Definir la función delta como un vector de ceros
delta = zeros(size(n));

% Asignar 1 a las posiciones correspondientes
index = find(n == -2);
delta(index) = 1;
index = find(n == -1);
delta(index) = 1;
index = find(n == 0);
delta(index) = 1;

% Definir la señal de entrada x
x = cos(2 * pi * t);

% Definir el sistema h utilizando los valores de delta
h = [1/2 * delta(n == -2), -2 * delta(n == -1), 3/2 * delta(n == 0)];
h=[-0.5,2,-1.5];

% Realizar la convolución
y = conv(x, h, 'same'); % 'same' para mantener el tamaño de y igual al de x

% Graficar el resultado
plot(t, y);
xlabel('Time (s)');
ylabel('Amplitude');
title('Output y(t)');
grid on;
hold on
plot(t,x);

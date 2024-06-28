% Definir la señal de entrada x (usar 'B' como la señal de entrada)
x = B;

% Definir el sistema h (según el código proporcionado)
h = -0.5:0.1:0.5;

% Realizar la convolución
y = conv(x, h, 'same'); % 'same' para mantener el tamaño de y igual al de x

% Establecer un umbral para la detección de picos
threshold = 400; % Puedes ajustar este valor según sea necesario

% Detectar los picos que superan el umbral
[pks, locs] = findpeaks(y, 'MinPeakHeight', threshold);

% Graficar el resultado de la convolución
figure;
plot(y);
hold on;
plot(locs, pks, 'r^', 'MarkerFaceColor', 'r'); % Marcar los picos detectados
xlabel('Time (s)');
ylabel('Amplitude');
title('Output y(t) with Peaks');
grid on;
hold off;

% Graficar la señal de entrada
figure;
plot(x);
xlabel('Time (s)');
ylabel('Amplitude');
title('Input Signal x(t)');
grid on;

fprintf('los valores donde se encuentran los picos son: ');
disp(locs);
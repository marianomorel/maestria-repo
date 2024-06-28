% Paso 1: Especificar la señal de entrada
Fs = 1000;               % Frecuencia de muestreo
t = 0:1/Fs:5;            % Tiempo discreto de 5 segundos
f = 10;                  % Frecuencia del coseno en Hz
x = cos(2*pi*f*t);       % Señal de entrada

figure;
plot(t, x);
title('Señal de entrada x[n]');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Paso 2: Generar la salida deseada del sistema "desconocido"
h = [3/2, -2, 1/2];      % Respuesta al impulso del sistema
d = conv(x, h, 'same');  % Salida deseada mediante la convolución

figure;
plot(t, d);
title('Salida deseada d[n]');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Paso 3: Armar el algoritmo de aprendizaje LMS
alpha = 0.01;              % Constante adaptativa
L = 10;                    % Largo del sistema
w = randn(1, L);           % Vector de pesos iniciales aleatorios

% Inicializa las variables
N = length(x);
y = zeros(1, N);           % Salida del sistema adaptativo
e = zeros(1, N);           % Error

% Paso 4: Iterar el algoritmo LMS
num_iterations = 500;     % Número de iteraciones
LARGO = 5;                 % Duración en segundos

for k = 1:LARGO*Fs - L + 1
    y(k) = w * (x(k+L-1:-1:k))';      % Salida del sistema adaptativo
    e(k) = d(k) - y(k);               % Error
    w = w + alpha * e(k) * x(k+L-1:-1:k);  % Actualización de los pesos
end

% Graficar la salida del sistema adaptativo después del entrenamiento
figure;
plot(t(1:LARGO*Fs - L + 1), d(1:LARGO*Fs - L + 1), 'b', t(1:LARGO*Fs - L + 1), y(1:LARGO*Fs - L + 1), 'r--');
legend('Salida deseada d[n]', 'Salida del sistema adaptativo y[n]');
title('Salida del sistema adaptativo después del entrenamiento');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Graficar el error
figure;
plot(t(1:LARGO*Fs - L + 1), e(1:LARGO*Fs - L + 1));
title('Error de aprendizaje e[n]');
xlabel('Tiempo (s)');
ylabel('Amplitud');

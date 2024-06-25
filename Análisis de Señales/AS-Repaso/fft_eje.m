% Definir el intervalo de tiempo
t = -5:0.01:5; % desde -5 hasta 5 con pasos de 0.01

% Definir la funci�n por tramos
y = zeros(size(t));
y(t >= 0) = exp(-2*t(t >= 0));
y(t < 0) = exp(2*t(t < 0));

% Graficar la funci�n para verificar
figure;
plot(t, y);
title('Funci�n por tramos');
xlabel('t');
ylabel('y(t)');

% Calcular la FFT de la funci�n
Y = fft(y);

% Calcular el vector de frecuencias
n = length(t);
f = (-n/2:n/2-1)*(1/(n*0.01));

% Shift FFT para centrar las frecuencias en cero
Y_shifted = fftshift(Y);

% Graficar la magnitud de la FFT
figure;
plot(f, abs(Y_shifted));
title('FFT de la funci�n por tramos');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');

%pasa altos de dos polos
Fs = 200;   % Frecuencia de muestreo
Fc = 5;
r=0.5;
tita=2*pi*(Fc/Fs);
B=A;
% Coeficientes del filtro Notch FIR dado
b1=2*r*cos(tita);
b2=r^2;
a1=-2;
a2=1;
Z = [1, a1, a2];             % Numerador (ceros en z = -1)
P = [1,-b1, b2];             % Denominador (polo doble en el origen)

% Respuesta al impulso
hz = (impz(Z, P))';

% Filtrado de la señal
output = filtfilt(Z, P, A);

% Gráfica temporal de entrada y salida
figure;
subplot(3,1,1);
plot(A);
title('Señal con ruido');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(3,1,2);
plot(output);
title('Señal filtrada');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(3,1,3);
stem(hz);
title('Respuesta al impulso del filtro');
xlabel('n');
ylabel('h[n]');

% Diagrama de polos y ceros
figure;
zplane(Z, P);
title('Diagrama de polos y ceros');

% Respuesta en frecuencia
figure;
freqz(Z, P, 1024, Fs);
title('Respuesta en frecuencia');

%otra forma%

for i=3:length(A)
B(i)=b1*B(i-1)-b2*B(i-2)+A(i)+a1*A(i-1)+a2*A(i-2);% resp al impulso en n
end
figure;
plot(B,'g')
hold on
plot(A,'r')

%otra forma%

C=conv(A,hz); %si conociera h, no uso impz
plot(C,'r')
hold on
plot(A,'b')

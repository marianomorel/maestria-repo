%filtro notch a 50hz

Fs = 200;                 % Frecuencia de muestreo
t = 0:1/Fs:10;            % Vector de tiempo

% Se�al original y ruido
senal = sin(2*pi*0.1*t);   % Se�al de ejemplo a 0.1 Hz
ruido = 0.1*sin(2*pi*50*t); % Ruido a 50 Hz
syr = senal + ruido;       % Se�al con ruido

% Coeficientes del filtro Notch FIR dado
b = [1, 0, 1];             % Numerador (ceros en z = -1)
a = [1, 0, 0];             % Denominador (polo doble en el origen)

% Respuesta al impulso
hz = 0.5*impz(b, a);

% Filtrado de la se�al
output = filter(b, a, syr);

% Gr�fica temporal de entrada y salida
figure;
subplot(3,1,1);
plot(t, syr);
title('Se�al con ruido');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(3,1,2);
plot(t, output);
title('Se�al filtrada');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(3,1,3);
stem(h);
title('Respuesta al impulso del filtro');
xlabel('n');
ylabel('h[n]');

% Diagrama de polos y ceros
figure;
zplane(b, a);
title('Diagrama de polos y ceros');

% Respuesta en frecuencia
figure;
freqz(b, a, 1024, Fs);
title('Respuesta en frecuencia');

%otra forma de generar la se�al filtrada

B=A; %se�al materna
for i=3:length(A)
B(i)=0.5*(A(i)+A(i-2));% resp al impulso en n
end
figure;
plot(B,'g')
hold on


%otra forma de generar la se�al filtrada

h=[0.5 0 0.5];
C=conv(A,h);
plot(C,'r')
hold on
plot(A,'b')
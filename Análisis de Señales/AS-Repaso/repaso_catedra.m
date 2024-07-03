% Ejercicio resuelto

clearvars
close all
clc

% Carga de se?al. Definici?n de Fs y espacio de tiempo n

load('SIGNALSADQ.mat')
Fs = 1000;
n = 0:1/Fs:length(s)/Fs - 1/Fs;

plot(s)

% Filtro pasa altos para eliminar deriva lenta

Fc = 0.4;
Fs = 1000;
tita = 2*pi*(Fc/Fs);
r = 0.995;
b1 = 2*r*cos(tita);
b2 = r*r;
a1 = -2;
a2 = 1;
num = [1 a1 a2]; % z2 z1
den = [1 -b1 b2]; % z2 z1

figure(2);
zplane(num,den)
grid

figure(3);
freqz(num, den, 2000, 1000)

C = filtfilt(num,den,s);

figure(1);
hold on;
plot(C,'m');
hold off;

% Observación de la FFT para analizar los ruidos

% Si no queremos que se vea pulsada, puede hacerse una FFT de sólo una
% subseñal (un "período" solamente)... lo que se ve pulsado es por la
% repetición de las señales.

% Se observan los picos de 50Hz y sus armónicos impares (señal de simetría
% de media onda (sólo los n impares de la serie de Fourier)

figure(4)
w = 0 : 2*pi/length(C) : 2*pi - 2*pi/ length(C);
f = linspace(0,Fs,length(C));
plot(abs(fft(C)))

% Filtro Notch

fase = pi/10;
z1 = 1 .* exp(1j*fase);
z2 = 1 .* exp(1j*-fase);
fase = 3*pi/10;
z3 = 1 .* exp(1j*fase);
z4 = 1 .* exp(1j*-fase);
z5 = 1j;
z6 = -1j;
fase = 7*pi/10;
z7 = 1 .* exp(1j*fase);
z8 = 1 .* exp(1j*-fase);
fase = 9*pi/10;
z9 = 1 .* exp(1j*fase);
z10 = 1 .* exp(1j*-fase);
ceros = [z1 z2 z3 z4 z5 z6 z7 z8 z9 z10];
num = poly(ceros);
den = [1 0 0 0 0 0 0 0 0 0 0];
% den = zeros(1,length(num));
% den(1) = 1;

G = (sum(num)/sum(den)); % La ganancia de continua sería cuando z = 1 (z = e^(jw) con w = 0)

figure(5);
zplane(num,den)
grid
figure(6)
freqz(num, den, 2000, 1000)

salida1 = filter(num,den,C)/G;

figure(1);
hold on;
plot(salida1,'k');
hold off;

% Búsqueda de marcas en la señal adjunta de estímulo (referencia)

i = 1;
k = 0;
marcas = zeros(1,40);
while(i<length(estimulo))
    
    if (estimulo(i) >= 0.5)
        k = k + 1;
        marcas(k) = i;
        i = i + 11;
    end
    i = i + 1;
       
end
marcas = marcas(1:k);

% Promediador de señal

largo = marcas(2) - marcas(1); % podría usar un mínimo si es variable (estímulo no períodico)

% plot(salida1(1:marcas(2)));
ref = salida1(1:marcas(2));
seleccionados = zeros(1,10);
pa = zeros(1,largo);
p = 0;
for i = 2 : k-1
    plot(ref);hold on;plot(salida1(marcas(i):marcas(i+1)-1),'r');hold off;
    corr = corrcoef(ref,salida1(marcas(i):marcas(i+1)));
    if (corr(1,2)>0.9)
        p = p + 1;
        seleccionados(p) = i;
        pa = pa + salida1(marcas(i):marcas(i+1)-1);
    end
    if (p >= 10)
        break;
    end
%     pause;
end
pa = pa/10;
plot(pa);

% Filtro pasa bajos

ceros = [-1 -1]; % Quiero un Pasa Bajos
r = 0.92;
fc = 20; % Frecuencia de corte en 20Hz
tita = fc*2*pi/Fs; % Regla de 3 - Todo el c?rculo es Fs = 1000Hz
polos = [r.*exp(1j*tita) r.*exp(1j*-tita)]; % Siempre van conjugados para que el polinomio de real
num = poly(ceros);
den = poly(polos);
G = (sum(num)/sum(den)); % La ganancia de continua sería cuando z = 1 (z = e^(jw) con w = 0)
pa = filter(num,den,pa);
pa = pa/(G);
hold on;
plot(pa,'r');
hold off;

% Derivada de 3 puntos para hallar la pendiente de subida del potencial de
% acción

h = [3 -4 1];

salidafinal = conv(pa,h);
hold on;
plot(salidafinal(1 : end - length(h)),'m');
hold off;

[M,pos] = max(salidafinal(1 : end -length(h)));
hold on;
stem(pos,M,'kx','LineWidth',2);
hold off;
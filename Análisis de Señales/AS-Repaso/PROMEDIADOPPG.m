% Promediado de PPG
clearvars
close all
clc
load('multi2.mat');
salidaoscu = PCG;
salida2 = PPG;
Fc = 30;
Fs = 200;
tita = 2*pi*(Fc/Fs);
r = 0.5;
b1 = 2*r*cos(tita);
b2 = r*r;
a1 = -2;
a2 = 1;
ceros = [1 a1 a2]; % z2 z1
polos = [1 -b1 b2]; % z2 z1
salidaoscu = filtfilt(ceros,polos,salidaoscu);
ceros = [1/4 1/2 1/4]; % z2 z1
polos = [1 0 0]; % z2 z1
salidaoscu = filtfilt(ceros,polos,salidaoscu);
subplot(2,1,1);
plot(salida2);
subplot(2,1,2);
plot(salidaoscu);

i = 1;
marcas = ones(1,10);
k = 0;
while(i < length(salidaoscu))
if (salidaoscu(i) > 0.71)
k = k + 1;
marcas(k) = i;
i = i + 100;
end
i = i + 1;
end
hold on;
stem(marcas,ones(1,length(marcas)),'r');
hold off;
RR = floor(mean(diff(marcas)));

% Promediado
clear zeros;
L = RR-10;
vector = zeros(1,L);
for i = 1 : length(marcas) - 1
vector = vector + salida2(marcas(i) : marcas(i) + L - 1);
end
vector = vector / (length(marcas) - 1);
figure;
plot(vector);

%vuelve a filtrar
ceros = [1/16 1/4 6/16 1/4 1/16]; % z2 z1
polos = [1 0 0 0 0]; % z2 z1
vector = filtfilt(ceros,polos,vector);
hold on;
plot(vector,'r');
hold off;

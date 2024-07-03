% Carga de señal. Definicion de Fs y espacio de tiempo n

%load('SIGNALSADQ.mat')
Fs = 1000;
% n = 0:1/Fs:length(A)/Fs - 1/Fs; 

% Filtro pasa bajos

b1 = 0;
b2 = 0;
a1 = 0;
a2 = 1;
num = [1 a1 a2]; % z2 z 1
den = [1 -b1 b2]; % z2 z 1

figure(2);
zplane(num,den)
grid

figure(3);
freqz(num, den, 2000, Fs)

C = filtfilt(num,den,A);

figure(1);
plot(C,'m'); 
hold on;
plot(A,'g')
hold off;

%FILTRO CON ECUACION EN DIFERENCIAS

B=A;

for i=3:length(A)
B(i)=0.25*(A(i)+A(i-2));% resp al impulso en n
end
figure;
plot(B,'r')
hold on
plot(0.5*A,'g')
% Ejercicio resuelto

% Carga de se?al. Definici?n de Fs y espacio de tiempo n

%load('SIGNALSADQ.mat')
Fs = 20;
n = 0:1/Fs:length(A)/Fs - 1/Fs; %para que lo uso?

% Filtro pasa bajos

b1 = 0;
b2 = 0;
a1 = 2;
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
plot(n,0.1*C,'m'); %no uso n?
hold on;
plot(n,A,'g')
hold off;



% Fs = 8; %para que lo uso?
% n = 0:1/Fs:length(A)/Fs - 1/Fs; %para que lo uso?
% B=A;
% 
% for i=3:length(A)
% B(i)=(A(i)+2*A(i-1)+A(i-2))/Fs;% resp al impulso en n
% end
% figure;
% plot(B,'g')
% hold on
% plot(0.5*A,'r')

%filtro iir de un solo polo con T con x=t^2
clearvars
close all
clc
Fs = 200;
t = -4 : 1/Fs : 4;
x = t.*t;
y = zeros(length(t));
for i = 2 : length(t) 
    y(i) = y(i-1) + x(i)/Fs; %T=1/Fs
end
plot(t,x);
hold on;
plot(t,y,'m');
hold off;
num = [1 0];
den = [1 -1];
figure;
zplane(num,den);
figure;
freqz(num,den,2000,200);
clearvars
close all
clc
% Coseno FFT% 
Fs = 200;
f = 10;
n = 0 : 1/Fs : 1;
L = length(n);
x = cos(2*pi*f*n);
subplot(1,2,1);
plot(n,x);

X = fft(x);
w = 0 : 2*pi/L : 2*pi - 2*pi/L;
subplot(1,2,2);
plot(w,abs(X));

% Pulso FFT
Fs = 200;
n = 0 : 1/Fs : 1;L = length(n);
%p1 = ones(1,20);
%p2 = zeros(1,L-20);
%p = [p1 p2];
p = zeros(1,L);
p(1:20) = ones(1,20);
subplot(1,2,1);
stem(n,p);
P = fft(p);
w = 0 : 2*pi/L : 2*pi - 2*pi/L;
subplot(1,2,2);
plot(w,abs(P));
clear all; 
clf;

% Pulso FFT
Fs = 200;
n = 0 : 1/Fs : 1;
L = length(n);
p = zeros(1,L);
p(1:20) = ones(1,20);
subplot(2,1,1);stem(n,p);
P = fft(p);
w = 0 : 2*pi/L : 2*pi-2*pi/L;
subplot(2,1,2);
plot(w,abs(P));
% pause;
% yy = upsample(p,2);
% yy = yy(1:end-1);
% n = 0 : 1/(2*Fs) : 1;
% L = length(n);
% subplot(2,1,1);stem(n,yy);
% YY = fft(yy);
% w = 0 : 2*pi/L : 2*pi-2*pi/L;
% subplot(2,1,2);plot(w,abs(YY));
%Gabor_1.m
% representar para alfa = 1, 2 y 1/4 con beta= 0, 1 y 1/2.
%Representar su TF y observar la relación entre los desvíos
%(de la función Gaussiana) en los dominios temporal y 
%frecuencial.  



% Ventana de Gabor y su espectro 
% representar para alfa = 1, 2 y 1/4 con beta= 0, 1 y 1/2
% gw = exp(-(t-beta).^2/4*alfa).*(1/(2*sqrt(pi*alfa)));
clc;
clf;
% variable independiente entre -8 y 8
fs=16;
t = -8:1/fs:8-1/fs;                   % paso de 0.0625 (1/16), seria como Fs =16, 256 muestras
gw1 = exp(-t.^2/4).*(1/(2*sqrt(pi))); % ventana de Gabor alfa 1 y beta =0
gw2 = exp(-t.^2).*(1/(2*sqrt(pi/4))); % ventana de Gabor alfa 0.25 y beta =0
 
subplot(1,2,1)
plot(t,gw1,t,gw2,'r'), xlabel('tiempo'), ylabel('Ventana de Gabor')

 
%Espectro de Ventana de Gabor
 
espgw1=abs(fft(gw1));%256 muestras
espgw2=abs(fft(gw2));%256 muestras
L = length(espgw1);
 
f = (0:L-1)*(fs/L);
 
subplot(1,2,2)
plot(f,espgw1,f,espgw2),  xlabel('Hertz'), ylabel('Ventana de Gabor')

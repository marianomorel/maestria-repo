%transformada de Fourier con Ventana Deslizante
clear all; 
clf;

t1=0:1/128:1;
t2=1:1/128:2;
t=[t1 t2];
f1=2*sin(2*pi*32*t1); f2=sin(2*pi*8*t2); f=[f1 f2];
alfa=1/64;
G=[];

for j = 1 : 16
g=(1/(2*sqrt(pi*alfa))*exp(-(t-j/8).^2)/(4*alfa));

% genera matriz G que contiene 16 transformadas
a=f.*g; d=abs(fft(a)); G=[G;d(1:128)];
end
mesh(G);



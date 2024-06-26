%transformada de Fourier con Ventana 
clear all; 
clf;

t1=0:1/128:1;
t2=1:1/128:2;
t=[t1 t2];
f1=2*sin(2*pi*32*t1); f2=sin(2*pi*8*t2); f=[f1 f2];
% alfa=input('ingrese alfa ');
% n=input('ingrese n ');

alfa = (1/2);
n = 0.5;
g=( 1/(2*sqrt(pi*alfa))*exp(-(t-n)).^2/(4*alfa) );
a=f.*g;
b=abs(fft(f));c=abs(fft(g));d=abs(fft(a));
b1=b(1:128);c1=c(1:128);d1=d(1:128);
x=0:1/256:0.5-1/256;

subplot(221),plot(t,f,t,g);
subplot(222),plot(t, a);
subplot(223),plot(x,b1,x,c1);
subplot(224),plot(x,d1);


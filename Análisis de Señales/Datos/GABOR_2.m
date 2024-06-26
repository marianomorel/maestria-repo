% Análisis de señales con Ventana de Gabor 

clear all; 
clf;

% variable independiente entre -4 y 4
t = -4:1/64:4-1/64;   % 512 puntos
alfa = 1/16;
gw=exp(-t.^2/(4*alfa)).*(1/(2*sqrt(pi*alfa)));
senal=3*sin(4*pi*t)+cos(8*pi*t);%f1=2, f2=4

subplot(221)
plot(t,gw,t,senal);
xlabel('tiempo');
ylabel('ventana de Gabor');
grid

subplot(222)

plot(t,senal.*gw);
xlabel('tiempo');
ylabel('producto = senal X ventana Gabor');

subplot(223)
espsenal = abs(fft(senal));
f= 0: 1/256 : 0.5 - 1/256; % 128 puntos
plot(f,espsenal(1:128));

espwf=abs(fft(gw.*senal));
subplot(224)
plot(f,espwf(1:128));

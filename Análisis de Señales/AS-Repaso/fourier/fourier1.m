%%
% Ejemplo Computo de arm�nicos y frecuencias
clear all; 
syms t
% se�al
y=1+sin(100*t);
T0=2*pi/100; 
N=5; % N arm�nicos

figure(1)
subplot(211)
fplot(y,[0,0.25]); grid; xlabel('t (s)'); ylabel('y(t)')

% computo arm�nicos y frecuencias 
[Y1, w1]=fourierseries(y,T0,N);
Y=[conj(fliplr(Y1(2:N))) Y1];
w=[-fliplr(w1(2:N)) w1];

subplot(223)
stem(w,abs(Y)); grid; axis([-400 400 -0.1 1.1])

xlabel('k\Omega_0 (rad/s)'); ylabel('|Y_k|')

subplot(224)
stem(w,angle(Y)); grid; axis([-400 400 -2 2])

xlabel('k\Omega_0 (rad/s)'); ylabel('\angle{Y_k}')



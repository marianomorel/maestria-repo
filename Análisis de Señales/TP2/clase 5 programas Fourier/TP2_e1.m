% Ejemplo 1 Computo de armónicos y frecuencias
clear all; 
syms t
% señal
y=1+sin(100*t);
T0=2*pi/100; 
N=10; % N armónicos
figure(1)
subplot(211)
fplot(y,[0,0.25]); grid; xlabel('t (s)'); ylabel('y(t)')
% computo armónicos y frecuencias 
[Y1, w1]=fourierseries(y,T0,N);
Y=[conj(fliplr(Y1(2:N))) Y1];
w=[-fliplr(w1(2:N)) w1];
subplot(223)
stem(w,abs(Y)); grid; axis([-400 400 -0.1 1.1])
xlabel('k\Omega_0 (rad/s)'); ylabel('|Y_k|')
subplot(224)
stem(w,angle(Y)); grid; axis([-400 400 -2 2])
xlabel('k\Omega_0 (rad/s)'); ylabel('\angle{Y_k}')



%##########################################################%


clear all;
clf
syms t
T0=1; %periodo fundamental 
N=10; %cantidad de armónicos  
% construyo la señal con escalones 
m=heaviside(t)-heaviside(t-T0/8)+heaviside(t-7*T0/8);
x=abs(cos(pi*t));

% armónicos y frecuencias de los armónicos
[X1,w1]=fourierseries(x,T0,N);
X=[conj(fliplr(X1(2:N))) X1];
w=[-fliplr(w1(2:N)) w1];
figure(1)
subplot(221)
fplot(x,[-T0/2 T0/2],'LineWidth',2);grid; 
title('periodo de x(t)')
subplot(222)
stem(w,X); grid; axis([min(w) max(w) -0.5 1.1]); 
title('real X(k)'); xlabel('k\Omega_0 (rad/s)'); ylabel('X_k')
subplot(223)
stem(w,abs(X)); grid; 
title('magnitud coef. de Fourier')
axis([min(w) max(w) -0.1 1.1])
xlabel('k\Omega_0 (rad/s)'); ylabel('|X_k|')
subplot(224)
stem(w,[-angle(X1(2:N)) angle(X1)]); grid; 
title('fase coef. de Fourier')
axis([min(w) max(w) -3.5 3.5])
xlabel('k\Omega_0 (rad/s)'); ylabel('\angle{X_k}')


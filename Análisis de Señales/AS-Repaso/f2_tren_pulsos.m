%Ejemplo 2 # Serie de Fourier---Computo de armónicos y frecuencias armónicas 
%de un tren de pulsos. 

clear all;
clf
syms t
T0=1; %periodo fundamental 
N=20; %cantidad de armónicos  
% construyo la señal con escalones 
m=heaviside(t)-heaviside(t-T0/4)+heaviside(t-3*T0/4);
x=2*m;
% armónicos y frecuencias de los armónicos
[X1,w1]=fourierseries(x,T0,N);
X=[conj(fliplr(X1(2:N))) X1];
w=[-fliplr(w1(2:N)) w1];
figure(1)
subplot(221)
fplot(x,[0 T0],'LineWidth',2);
grid; 
title('periodo de x(t)')
subplot(222)
stem(w,X); 
grid; 
axis([min(w) max(w) -0.5 1.1]); 
title('real X(k)'); xlabel('k\Omega_0 (rad/s)'); 
ylabel('X_k')
subplot(223)
stem(w,abs(X)); 
grid; 
title('magnitud coef. de Fourier')
axis([min(w) max(w) -0.1 1.1])
xlabel('k\Omega_0 (rad/s)'); 
ylabel('|X_k|')
subplot(224)
stem(w,[-angle(X1(2:N)) angle(X1)]); 
grid; 
title('fase coef. de Fourier')
axis([min(w) max(w) -3.5 3.5])
xlabel('k\Omega_0 (rad/s)'); 
ylabel('\angle{X_k}')

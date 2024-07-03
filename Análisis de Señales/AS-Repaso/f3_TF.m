% Ejemplo 3 Tiempo vs. Frecuencia. Transformada de Fourier

% Graficar el cambio que se produce en la 
% Transformada de Fourier a medida que el 
% soporte de la senal en el tiempo se 
% incrementa de [-0.5 a 0.5] hasta [-2 a 2]

clear all; 
clf
syms t w
for i=1:2,
tau=0.5+(i-1)*1.5; 
x=heaviside(t+tau)-heaviside(t-tau); 
X=fourier(x);
if(i==1)
figure(1)
subplot(211)
 
fplot(x,[-3 3]);
axis([-3 3 -0.1 1.1]);
grid
ylabel('x_1(t)');
xlabel('t');
subplot(212)
 
fplot(X,[-50 50]);
axis([-50 50 -1 5]);
grid
ylabel('X_1(\Omega)');
xlabel('\Omega')
else
    
figure(2) 
subplot(211)
fplot(x,[-3 3]);
axis([-3 3 -0.1 1.1]);
grid; ylabel('x_2(t)');xlabel('t');
subplot(212) 
fplot(X,[-50 50]);
axis([-50 50 -1 5]);
grid; ylabel('X_2(\Omega)');xlabel('\Omega')
 
end
 
end

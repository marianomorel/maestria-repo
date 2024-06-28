clear all;
clf;
syms t;
T0 = 1; % periodo fundamental 
N = 2; % cantidad de arm�nicos  

% construyo la se�al con escalones  
%m = heaviside(t) - heaviside(t - T0/4) +  heaviside(t - 3*T0/4); 
%m = heaviside(t) - heaviside(t - 1*T0/2);
%m = heaviside(t) - heaviside(t - 4*T0/10) +  heaviside(t - 6*T0/10);
m=abs(cos(1*pi*t))
x = m;

% arm�nicos y frecuencias de los arm�nicos
[X1, w1] = fourierseries(x, T0, N);
X = [conj(fliplr(X1(2:N))) X1];
w = [-fliplr(w1(2:N)) w1];

% Convertir a double para la interpolaci�n
real_X = double(real(X));
w = double(w);

% Interpolaci�n suave
interp_points = linspace(min(w), max(w), 1000);
real_X_interp = interp1(w, real_X, interp_points, 'spline');

figure(1);
subplot(221);
fplot(x, [-T0/2 T0/2], 'LineWidth', 2); 
grid; 
title('Periodo de x(t)');

subplot(222);
stem(w, real_X); 
hold on;
plot(interp_points, real_X_interp, 'r--', 'LineWidth', 1.5); % L�nea de interpolaci�n
grid; 
axis([min(w) max(w) -0.5 1.1]); 
title('Real X(k)'); 
xlabel('k\Omega_0 (rad/s)'); 
ylabel('X_k');
hold off;

subplot(223);
stem(w, abs(X)); 
grid; 
title('Magnitud coef. de Fourier');
axis([min(w) max(w) -0.1 1.1]);
xlabel('k\Omega_0 (rad/s)'); 
ylabel('|X_k|');

subplot(224);
stem(w, [-angle(X1(2:N)) angle(X1)]); 
grid; 
title('Fase coef. de Fourier');
axis([min(w) max(w) -3.5 3.5]);
xlabel('k\Omega_0 (rad/s)'); 
ylabel('\angle{X_k}');

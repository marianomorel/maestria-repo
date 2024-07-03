%serie de fourier para diferentes valores K de un coseno

clear all;
clf;
syms t;
T0 = 1; % periodo fundamental 
N = 10; % cantidad de armónicos  

% Valores de K a utilizar
K_values = [0.25, 0.0625, 2, 8];

figure(1);

for i = 1:length(K_values)
    K = K_values(i);
    % Construcción de la señal m(t) con el nuevo valor de K
    m = abs(cos(K * pi * t));
    x = m;

    % armónicos y frecuencias de los armónicos
    [X1, w1] = fourierseries(x, T0, N);
    X = [conj(fliplr(X1(2:N))) X1];
    w = [-fliplr(w1(2:N)) w1];

    % Convertir a double para la interpolación
    real_X = double(real(X));
    w = double(w);

    % Interpolación suave
    interp_points = linspace(min(w), max(w), 1000);
    real_X_interp = interp1(w, real_X, interp_points, 'spline');

    % Gráfico para el valor actual de K
    subplot(2, 2, i);
    stem(w, real_X); 
    hold on;
    plot(interp_points, real_X_interp, 'r--', 'LineWidth', 1.5); % Línea de interpolación
    grid; 
    axis([min(w) max(w) -0.5 1.1]); 
    title(['K = ' num2str(K)]); 
    xlabel('k\Omega_0 (rad/s)'); 
    ylabel('X_k');
    hold off;
end

% clear all;
% clf;
% syms t;
% T0 = 1; % periodo fundamental 
% N = 10; % cantidad de armónicos  
% 
% % Valores de K a utilizar
% K_values = [0.25, 0.0625, 2, 8];

figure(2);

for i = 1:length(K_values)
    K = K_values(i);
    % Construcción de la señal m(t) con el nuevo valor de K
    m = abs(cos(K * pi * t));
    x = m;

    % Gráfico para el valor actual de K
    subplot(2, 2, i);
    fplot(x, [-T0/2 T0/2], 'LineWidth', 2); 
    grid; 
    title(['K = ' num2str(K)]); 
    xlabel('t'); 
    ylabel('x(t)');
end


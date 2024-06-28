
% Tomar los primeros 39 elementos de pa para el c�lculo de la pendiente
datos_pa = pa(23:40);
indices = 22:39;

% Calcular la derivada num�rica
dy = diff(datos_pa);  % Diferencias en el eje y
dx = diff(indices);    % Diferencias en el eje x

% Calcular la pendiente como el cociente entre dy y dx
pendiente = dy / dx;

% Mostrar la pendiente encontrada
disp(['La pendiente calculada usando derivada num�rica es: ', num2str(pendiente)]);

% Graficar los datos originales de pa y la regi�n donde se calcula la pendiente
figure;
plot(pa, 'b-');  % Curva completa de pa en azul
hold on;

% Graficar la l�nea de la pendiente calculada sobre la curva completa de pa
x_line = [indices(1), indices(end)];  % Extremos del intervalo de �ndices
y_line = pa(indices(1)) + pendiente * (x_line - indices(1));  % Ecuaci�n de la recta sobre pa completa
plot(x_line, y_line, 'r-', 'LineWidth', 2);  % L�nea verde

% Configurar el gr�fico
title('Curva de pa con c�lculo de pendiente');
xlabel('�ndices');
ylabel('pa');
legend('Curva completa de pa', 'Regresi�n sobre pa');
grid on;
hold off;

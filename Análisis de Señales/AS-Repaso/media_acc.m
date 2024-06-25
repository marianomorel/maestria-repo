
y = zeros(1,200); % Inicialización de y
x = randn(1, 200); % Señal aleatoria

for i = 2:length(x) % Recorrer desde 1 hasta la longitud de x
    y(i) = (i/(i+1))*y(i) + (1/(i+1))*x(i);
end
plot(x);
hold on
plot(y)
disp(y); % Mostrar el valor final de y

%eje1_ total

                 %########### INCISO A #############%
%el codigo calcula una media (f(t)=k1) para los primeros 10 valores y despues desde
%la muestra numero 20 aproxima una funcion exponencial decreciente de la
%forma g(t)=k2+a*exp^(b*t)

% Definir los datos
datos = [1.104242446, 1.150798155, 1.138958902, 1.137055193, 1.15809877, 1.160113132, 1.155232025, 1.122248314, 1.131654522, 1.152655958, 1.107690319, 1.107681966, 1.118891856, 1.136724614, 1.168085575, 1.149728608, 1.121830196, 1.120401999, 1.159525014, 1.16381532, 1.134726131, 1.082172296, 1.062528241, 1.044050668, 1.06954052, 1.025026354, 1.032259119, 0.970729014, 0.929459491, 0.966265028, 0.926573318, 0.979828243, 0.963328536, 0.900278147, 0.852609963, 0.907118779, 0.914228981, 0.918838469, 0.819154899, 0.850823286, 0.856885816, 0.860633976, 0.857695716, 0.844959121, 0.847241046, 0.806894344, 0.822968509, 0.772040575, 0.762108804, 0.850510731, 0.777464944, 0.805168477, 0.838799505, 0.758282327, 0.756324213, 0.768681845, 0.825473632, 0.76907477, 0.755300959, 0.741282424, 0.764034909, 0.760151817, 0.734257762, 0.763220743, 0.727535019, 0.778603547, 0.717079933, 0.772227578, 0.792867089, 0.736491454, 0.756880925, 0.76819816, 0.716641082, 0.759419898, 0.7733606, 0.730638468, 0.791642082, 0.804507409, 0.791536896, 0.757033097, 0.733885792, 0.780254435, 0.72890765, 0.800596599, 0.766559369, 0.764253096, 0.721201569, 0.712709348, 0.728952464, 0.789051662, 0.794085339, 0.772740636, 0.775107735, 0.725403041, 0.759856548, 0.783161818, 0.742341438, 0.800668716, 0.710701304, 0.733680499, 0.752620039];

% Calcular la media de los primeros 10 datos
f = mean(datos(1:10));

% Datos desde la muestra n�mero 20 en adelante
t = (20:length(datos))';
y = datos(20:end)';

% Definir la funci�n exponencial decreciente
exp_fun = @(b,t) b(1) + b(2) * exp(b(3) * t);

% Inicializar par�metros [k2, a, b]
initial_guess = [min(y), max(y) - min(y), -0.1];

% Ajustar la funci�n a los datos
model = fitnlm(t, y, exp_fun, initial_guess);

% Obtener los par�metros ajustados
coefficients = model.Coefficients.Estimate;
k2 = coefficients(1);
a = coefficients(2);
b = coefficients(3);

% Definir la funci�n ajustada
g = @(t) k2 + a * exp(b * t);

% Encontrar la intersecci�n entre f y g(t)
intersection_func = @(t) f - g(t);
p_ini = fzero(intersection_func, 20); % Punto de inicio de b�squeda

% Calcular la funci�n ajustada para los 101 puntos
t_all = (1:length(datos))';
y_fit = g(t_all);

% Mostrar los resultados
fprintf('f = %.6f\n', f);
fprintf('k2 = %.6f\n', k2);
fprintf('a = %.6f\n', a);
fprintf('b = %.6f\n', b);
fprintf('p_ini = %.6f\n', p_ini);

% Graficar los datos originales, la media y la funci�n ajustada
figure;
plot(t_all, datos, 'bo', 'DisplayName', 'Datos originales');
hold on;
plot(t_all, f * ones(size(t_all)), 'r--', 'DisplayName', 'Media de los primeros 10 datos');
plot(t_all, y_fit, 'g-', 'DisplayName', 'Funci�n ajustada');
plot(p_ini, f, 'ko', 'MarkerFaceColor', 'k', 'DisplayName', 'Intersecci�n');
xlabel('Muestra');
ylabel('Valor');
title('Ajuste de la funci�n exponencial decreciente');
legend;
grid on;
hold off;


                         %########### INCISO B #############%
 % Definir los datos
datos = [1.104242446, 1.150798155, 1.138958902, 1.137055193, 1.15809877, 1.160113132, 1.155232025, 1.122248314, 1.131654522, 1.152655958, 1.107690319, 1.107681966, 1.118891856, 1.136724614, 1.168085575, 1.149728608, 1.121830196, 1.120401999, 1.159525014, 1.16381532, 1.134726131, 1.082172296, 1.062528241, 1.044050668, 1.06954052, 1.025026354, 1.032259119, 0.970729014, 0.929459491, 0.966265028, 0.926573318, 0.979828243, 0.963328536, 0.900278147, 0.852609963, 0.907118779, 0.914228981, 0.918838469, 0.819154899, 0.850823286, 0.856885816, 0.860633976, 0.857695716, 0.844959121, 0.847241046, 0.806894344, 0.822968509, 0.772040575, 0.762108804, 0.850510731, 0.777464944, 0.805168477, 0.838799505, 0.758282327, 0.756324213, 0.768681845, 0.825473632, 0.76907477, 0.755300959, 0.741282424, 0.764034909, 0.760151817, 0.734257762, 0.763220743, 0.727535019, 0.778603547, 0.717079933, 0.772227578, 0.792867089, 0.736491454, 0.756880925, 0.76819816, 0.716641082, 0.759419898, 0.7733606, 0.730638468, 0.791642082, 0.804507409, 0.791536896, 0.757033097, 0.733885792, 0.780254435, 0.72890765, 0.800596599, 0.766559369, 0.764253096, 0.721201569, 0.712709348, 0.728952464, 0.789051662, 0.794085339, 0.772740636, 0.775107735, 0.725403041, 0.759856548, 0.783161818, 0.742341438, 0.800668716, 0.710701304, 0.733680499, 0.752620039];

% Calcular la media de los primeros 10 datos
f = mean(datos(1:10));
%barrido de 20 valores para encontrar exponencial por ajuste

% Definir la funci�n exponencial decreciente
exp_fun = @(b, t) b(1) + b(2) * exp(b(3) * t);

% Inicializar par�metros [k2, a, b]
initial_guess = [min(datos), max(datos) - min(datos), -0.1];

% Ciclo de 20 posiciones cercanas a p_ini
for i = -10:10
    % Definir el intervalo temporal para cada ajuste
    t = (20 + i:length(datos))';
    y = datos(20 + i:end)';

    % Ajustar la funci�n a los datos
    model = fitnlm(t, y, exp_fun, initial_guess);

    % Obtener los par�metros ajustados
    coefficients = model.Coefficients.Estimate;
    k2 = coefficients(1);
    a = coefficients(2);
    b = coefficients(3);

    % Definir la funci�n ajustada
    g = @(t) k2 + a * exp(b * t);

    % Encontrar la intersecci�n entre f y g(t)
    intersection_func = @(t) f - g(t);
    p_ini = fzero(intersection_func, 20 + i); % Punto de inicio de b�squeda

    % Calcular la funci�n ajustada para los 101 puntos
    t_all = (1:length(datos))';
    y_fit = g(t_all);

    % Mostrar los resultados
    fprintf('Posici�n %d:\n', 20 + i);
    fprintf('f = %.6f\n', f);
    fprintf('k2 = %.6f\n', k2);
    fprintf('a = %.6f\n', a);
    fprintf('b = %.6f\n', b);
    fprintf('p_ini = %.6f\n\n', p_ini);

    % Graficar los datos originales, la media y la funci�n ajustada
    figure;
    plot(t_all, datos, 'bo', 'DisplayName', 'Datos originales');
    hold on;
    plot(t_all, f * ones(size(t_all)), 'r--', 'DisplayName', 'Media de los primeros 10 datos');
    plot(t_all, y_fit, 'g-', 'DisplayName', 'Funci�n ajustada');
    plot(p_ini, f, 'ko', 'MarkerFaceColor', 'k', 'DisplayName', 'Intersecci�n');
    xlabel('Muestra');
    ylabel('Valor');
    title(sprintf('Ajuste de la funci�n exponencial decreciente (Posici�n %d)', 20 + i));
    legend;
    grid on;
    hold off;
end

 
                            %########### INCISO C #############%
 % Definir los datos
datos = [1.104242446, 1.150798155, 1.138958902, 1.137055193, 1.15809877, 1.160113132, 1.155232025, 1.122248314, 1.131654522, 1.152655958, 1.107690319, 1.107681966, 1.118891856, 1.136724614, 1.168085575, 1.149728608, 1.121830196, 1.120401999, 1.159525014, 1.16381532, 1.134726131, 1.082172296, 1.062528241, 1.044050668, 1.06954052, 1.025026354, 1.032259119, 0.970729014, 0.929459491, 0.966265028, 0.926573318, 0.979828243, 0.963328536, 0.900278147, 0.852609963, 0.907118779, 0.914228981, 0.918838469, 0.819154899, 0.850823286, 0.856885816, 0.860633976, 0.857695716, 0.844959121, 0.847241046, 0.806894344, 0.822968509, 0.772040575, 0.762108804, 0.850510731, 0.777464944, 0.805168477, 0.838799505, 0.758282327, 0.756324213, 0.768681845, 0.825473632, 0.76907477, 0.755300959, 0.741282424, 0.764034909, 0.760151817, 0.734257762, 0.763220743, 0.727535019, 0.778603547, 0.717079933, 0.772227578, 0.792867089, 0.736491454, 0.756880925, 0.76819816, 0.716641082, 0.759419898, 0.7733606, 0.730638468, 0.791642082, 0.804507409, 0.791536896, 0.757033097, 0.733885792, 0.780254435, 0.72890765, 0.800596599, 0.766559369, 0.764253096, 0.721201569, 0.712709348, 0.728952464, 0.789051662, 0.794085339, 0.772740636, 0.775107735, 0.725403041, 0.759856548, 0.783161818, 0.742341438, 0.800668716, 0.710701304, 0.733680499, 0.752620039];

% Calcular la media de los primeros 10 datos
f = mean(datos(1:10));

% Definir la funci�n exponencial decreciente
exp_fun = @(b, t) b(1) + b(2) * exp(b(3) * t);

% Inicializar par�metros [k2, a, b]
initial_guess = [min(datos), max(datos) - min(datos), -0.1];

% Inicializar variables para almacenar la m�xima correlaci�n cruzada de f y g
max_corr_cross_f = -Inf;
max_corr_cross_g = -Inf;
max_corr_position_f = 0;
max_corr_position_g = 0;

% Ciclo de 20 posiciones cercanas a p_ini
for i = -10:10
    % Definir el intervalo temporal para cada ajuste
    t = (20 + i:length(datos))';
    y = datos(20 + i:end)';

    % Ajustar la funci�n a los datos
    model = fitnlm(t, y, exp_fun, initial_guess);

    % Obtener los par�metros ajustados
    coefficients = model.Coefficients.Estimate;
    k2 = coefficients(1);
    a = coefficients(2);
    b = coefficients(3);

    % Definir la funci�n ajustada
    g = @(t) k2 + a * exp(b * t);

    % Encontrar la intersecci�n entre f y g(t)
    intersection_func = @(t) f - g(t);
    p_ini = round(fzero(intersection_func, 20 + i)); % Punto de inicio de b�squeda

    % Calcular la correlaci�n cruzada entre f y los datos
    corr_cross_f = xcorr(f, datos(1:p_ini));
    % Calcular la correlaci�n cruzada entre g y los datos desde p_ini hasta el final
    corr_cross_g = xcorr(g(t(p_ini:end)), datos(p_ini:end));
    
    % Actualizar si se encuentra una nueva m�xima correlaci�n cruzada
    if max(corr_cross_f) > max_corr_cross_f
        max_corr_cross_f = max(corr_cross_f);
        max_corr_position_f = p_ini;
    end
    if max(corr_cross_g) > max_corr_cross_g
        max_corr_cross_g = max(corr_cross_g);
        max_corr_position_g = p_ini;
    end
    
    % Mostrar los resultados
    fprintf('Posici�n %d:\n', 20 + i);
    fprintf('f = %.6f\n', f);
    fprintf('k2 = %.6f\n', k2);
    fprintf('a = %.6f\n', a);
    fprintf('b = %.6f\n', b);
    fprintf('p_ini = %.6f\n', p_ini);
    %fprintf('Max correlaci�n cruzada entre f y datos: %.6f\n', max(corr_cross_f));
    %fprintf('Max correlaci�n cruzada entre g y datos desde p_ini hasta el final: %.6f\n\n', max(corr_cross_g));
end

% Mostrar la m�xima correlaci�n cruzada de f y g
fprintf('M�xima correlaci�n cruzada entre f y datos: %.6f en la posici�n %d\n', max_corr_cross_f, max_corr_position_f);
fprintf('M�xima correlaci�n cruzada entre g y datos desde p_ini hasta el final: %.6f en la posici�n %d\n', max_corr_cross_g, max_corr_position_g);
 
                    %########### INCISO D #############%

% Definir los datos
datos = [1.104242446, 1.150798155, 1.138958902, 1.137055193, 1.15809877, 1.160113132, 1.155232025, 1.122248314, 1.131654522, 1.152655958, 1.107690319, 1.107681966, 1.118891856, 1.136724614, 1.168085575, 1.149728608, 1.121830196, 1.120401999, 1.159525014, 1.16381532, 1.134726131, 1.082172296, 1.062528241, 1.044050668, 1.06954052, 1.025026354, 1.032259119, 0.970729014, 0.929459491, 0.966265028, 0.926573318, 0.979828243, 0.963328536, 0.900278147, 0.852609963, 0.907118779, 0.914228981, 0.918838469, 0.819154899, 0.850823286, 0.856885816, 0.860633976, 0.857695716, 0.844959121, 0.847241046, 0.806894344, 0.822968509, 0.772040575, 0.762108804, 0.850510731, 0.777464944, 0.805168477, 0.838799505, 0.758282327, 0.756324213, 0.768681845, 0.825473632, 0.76907477, 0.755300959, 0.741282424, 0.764034909, 0.760151817, 0.734257762, 0.763220743, 0.727535019, 0.778603547, 0.717079933, 0.772227578, 0.792867089, 0.736491454, 0.756880925, 0.76819816, 0.716641082, 0.759419898, 0.7733606, 0.730638468, 0.791642082, 0.804507409, 0.791536896, 0.757033097, 0.733885792, 0.780254435, 0.72890765, 0.800596599, 0.766559369, 0.764253096, 0.721201569, 0.712709348, 0.728952464, 0.789051662, 0.794085339, 0.772740636, 0.775107735, 0.725403041, 0.759856548, 0.783161818, 0.742341438, 0.800668716, 0.710701304, 0.733680499, 0.752620039];

% Calcular la media de los primeros 10 datos
f = mean(datos(1:10));

% Definir la funci�n exponencial decreciente
exp_fun = @(b, t) b(1) + b(2) * exp(b(3) * t);

% Inicializar par�metros [k2, a, b]
initial_guess = [min(datos), max(datos) - min(datos), -0.1];

% Inicializar variables para almacenar la m�xima correlaci�n cruzada de f y g
max_corr_cross_f = -Inf;
max_corr_cross_g = -Inf;
max_corr_position_f = 0;
max_corr_position_g = 0;

% Ciclo de 20 posiciones cercanas a p_ini
for i = -10:10
    % Definir el intervalo temporal para cada ajuste
    t = (20 + i:length(datos))';
    y = datos(20 + i:end)';

    % Ajustar la funci�n a los datos
    model = fitnlm(t, y, exp_fun, initial_guess);

    % Obtener los par�metros ajustados
    coefficients = model.Coefficients.Estimate;
    k2 = coefficients(1);
    a = coefficients(2);
    b = coefficients(3);

    % Definir la funci�n ajustada
    g = @(t) k2 + a * exp(b * t);

    % Encontrar la intersecci�n entre f y g(t)
    intersection_func = @(t) f - g(t);
    p_ini = round(fzero(intersection_func, 20 + i)); % Punto de inicio de b�squeda

    % Calcular la correlaci�n cruzada entre f y los datos
    corr_cross_f = xcorr(f, datos(1:p_ini));
    % Calcular la correlaci�n cruzada entre g y los datos desde p_ini hasta el final
    corr_cross_g = xcorr(g(t(p_ini:end)), datos(p_ini:end));
    
    % Actualizar si se encuentra una nueva m�xima correlaci�n cruzada
    if max(corr_cross_f) > max_corr_cross_f
        max_corr_cross_f = max(corr_cross_f);
        max_corr_position_f = p_ini;
    end
    if max(corr_cross_g) > max_corr_cross_g
        max_corr_cross_g = max(corr_cross_g);
        max_corr_position_g = p_ini;
    end
    
    % Mostrar los resultados
    fprintf('Posici�n %d:\n', 20 + i);
    fprintf('f = %.6f\n', f);
    fprintf('k2 = %.6f\n', k2);
    fprintf('a = %.6f\n', a);
    fprintf('b = %.6f\n', b);
    fprintf('p_ini = %.6f\n', p_ini);
    %fprintf('Max correlaci�n cruzada entre f y datos: %.6f\n', max(corr_cross_f));
    %fprintf('Max correlaci�n cruzada entre g y datos desde p_ini hasta el final: %.6f\n\n', max(corr_cross_g));
end

% Graficar los datos y las funciones f y g
t = (1:length(datos))'; % Intervalo temporal
figure;
plot(t, datos, 'b', 'LineWidth', 1.5); % Graficar datos
hold on;
plot(t(1:max_corr_position_f), f*ones(max_corr_position_f, 1), 'r--', 'LineWidth', 1.5); % Graficar f hasta p_ini
plot(t(max_corr_position_g:end), g(t(max_corr_position_g:end)), 'g--', 'LineWidth', 1.5); % Graficar g desde p_ini hasta el final
xlabel('Tiempo');
ylabel('Valor');
title('Datos y ajustes');
legend('Datos', 'f', 'g');
hold off;


% Mostrar la m�xima correlaci�n cruzada de f y g
fprintf('M�xima correlaci�n cruzada entre f y datos: %.6f en la posici�n %d\n', max_corr_cross_f, max_corr_position_f);
fprintf('M�xima correlaci�n cruzada entre g y datos desde p_ini hasta el final: %.6f en la posici�n %d\n', max_corr_cross_g, max_corr_position_g);

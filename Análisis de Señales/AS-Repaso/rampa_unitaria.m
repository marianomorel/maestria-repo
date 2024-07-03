function y = rampa_unitaria(t, t0_rampa)
    % Generar la rampa unitaria
    y = (t - t0_rampa) .* (t >= t0_rampa);

    % Graficar la rampa unitaria
    figure;
    plot(t, y, 'LineWidth', 2);
    title(['Rampa Unitaria que empieza en t = ', num2str(t0_rampa)]);
    xlabel('Tiempo');
    ylabel('Amplitud');
    grid on;
end

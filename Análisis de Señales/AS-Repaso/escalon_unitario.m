function y=escalon_unitario(t, t0_escalon)
    % Generar el escalón unitario
    u = t >= t0_escalon;
    y=u;
    % Graficar el escalón unitario
    figure;
    plot(t, u, 'LineWidth', 2);
    title(['Escalón Unitario que empieza en t = ', num2str(t0_escalon)]);
    xlabel('Tiempo');
    ylabel('Amplitud');
    grid on;
end

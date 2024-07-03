A=s; %señal cargada
Fs = 1000;   % Frecuencia de muestreo
Fc = 0.5; %frecuencia de corte
r=0.995;
tita=2*pi*(Fc/Fs);
% filtro pasa altos
b1=2*r*cos(tita);
b2=r^2;
a1=-2;
a2=1;
Z = [1, a1, a2];              
P = [1,-b1, b2];             

% Respuesta al impulso (en Z)
hz = (impz(Z, P))';

% Filtrado de la señal
output = filtfilt(Z, P, A);

% Gráfica temporal de entrada y output
figure;
subplot(3,1,1);
plot(A);
title('Señal con ruido');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(3,1,2);
plot(output);
title('Señal filtrada');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(3,1,3);
stem(hz);
title('Respuesta al impulso del filtro');
xlabel('n');
ylabel('h[n]');

% Diagrama de polos y ceros
figure;
zplane(Z, P);
title('Diagrama de polos y ceros con PA');

% Respuesta en frecuencia
figure;
freqz(Z, P, 1024, Fs);
title('Respuesta en frecuencia');


%filtro notch a 50hz
fi1=pi/10; %primer armonico
fi3=3*pi/10; %tercer armonico
fi5=5*pi/10; %5to armonico

z11=1*exp(1j*fi1); %ceros agregados para el primer armonico f=50hz
z12=1*exp(-1j*fi1);
z13=-1*exp(1j*fi1);
z14=-1*exp(-1j*fi1);

z31=1*exp(1j*fi3); %ceros agregados para el tercer armonico f=150hz
z32=1*exp(-1j*fi3);
z33=-1*exp(1j*fi3);
z34=-1*exp(-1j*fi3);

z51=1*exp(1j*fi5); %ceros agregados para el quinto armonico f=250hz
z52=1*exp(-1j*fi5);
%z53=-1*exp(1j*fi5);
%z54=-1*exp(-1j*fi5);

ceros=[z11 z12 z13 z14 z31 z32 z33 z34 z51 z52];
polos=[1 0 0 0 0 0 0 0 0 0];
ceros=poly(ceros);

%Diagrama de polos y ceros en el circulo unitario
zplane(ceros,polos);
title('Diagrama de P y Z de la señal filtrada PA + NOTCH');

output1 = filter(ceros, polos, output);
figure;
subplot(2,1,1);
plot(output1, 'r')
title('output filtrada por NOTCH');
subplot(2,1,2);
plot(output, 'b')
title('output filtrada por pasa altos');

figure;
subplot(2,1,1);
plot(abs(fft(output1)),'g') %FFT de la señal filtrada por NOTCH
title('FFT por NOTCH');
subplot(2,1,2);
plot(abs(fft(output)),'m') %FFT de la señal filtrada por pasa altos 
title('FFT por pasa altos');

figure;
freqz(ceros,polos,1024,Fs);
title('Respuesta en frecuencia (NOTCH)');

%############MARCAS###############%

i = 1;
k = 0;
marcas = zeros(1, 10);
while(i<length(estimulo))
    
    if (estimulo(i) >= 0.5)
        k = k + 1;
        marcas(k) = i;
        i = i + 11;
    end
    i = i + 1;
       
end
marcas = marcas(1:k);

largo = marcas(2) - marcas(1); % podr?a usar un m?nimo si es variable

%plot(output1(1:marcas(2)));
ref = output1(1:marcas(2));
seleccionados = zeros(1,10);
pa = zeros(1,largo);
p = 0;
for i = 2 : k-1
    plot(ref);hold on;plot(output1(marcas(i):marcas(i+1)-1),'r');
    hold off;
    corr = corrcoef(ref,output1(marcas(i):marcas(i+1)));
    if (corr(1,2)>0.9)
        p = p + 1;
        seleccionados(p) = i;
        pa = pa + output1(marcas(i):marcas(i+1)-1);
    end
    if (p >= 10)
        break;
    end
     pause;
end
pa = pa/10;
plot(pa);

%otro filtrado mas
zz1=1/16;
zz2=1/4;
zz3=6/16; 
zz4=1/4; 
zz5=1/16;
ceros2=[zz1 zz2 zz3 zz4 zz5];
%ceros2=poly(ceros2);
polos2 = [1 0 0 0 0]; % z2 z1
vector = filtfilt(ceros2,polos2,pa);
plot(vector,'r')
hold on;
plot(pa,'b');


% Tomar los primeros 39 elementos de pa
datos_pa = vector(23:40);

% Crear vector de índices desde 0 hasta 38
indices = 22:39;

% Realizar la regresión lineal utilizando polyfit
p = polyfit(indices, datos_pa, 1);  % Ajuste de polinomio de grado 1 (lineal)

% Obtener la pendiente y la ordenada al origen
pendiente = p(1);

% Mostrar la pendiente encontrada
disp(['La pendiente de la regresión lineal es: ', num2str(pendiente)]);

% Graficar los datos originales
figure;
plot(indices, datos_pa, 'bo', 'MarkerFaceColor', 'b');  % Puntos azules
hold on;

% Graficar la línea de regresión
y_fit = polyval(p, indices);
plot(indices, y_fit, 'r-', 'LineWidth', 2);  % Línea roja

% Configurar el gráfico
title('Regresión Lineal de los primeros 39 elementos de pa');
xlabel('Índices');
ylabel('Datos de pa');
legend('Datos originales', 'Regresión lineal');
grid on;
hold on;
plot(vector);
hold off;
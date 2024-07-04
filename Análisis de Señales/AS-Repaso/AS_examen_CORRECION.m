%%
%                             ######EJERCICIO 1########

figure;
plot(A);
title('Señal original');
% SUBMUESTREO
% Datos 
Fs = 1200; % Frecuencia de muestreo original
Ts = 1/Fs; % Período de muestreo

% TF de la señal original
F = fft(A);
L = length(F);
w = (0:L-1) * (Fs/L);

% Submuestreo de la señal
b = downsample(A, 2);
B = fft(b);

% Ajuste para la longitud y las frecuencias para la señal submuestreada
Lb = length(B);
Fsb = Fs / 2; % Nueva frec de muestreo
wb = (0:Lb-1) * (Fsb/Lb);

% subplot(2,1,1);
% plot(w, abs(F) / max(abs(F)));
% title('Señal original');
% xlabel('Frecuencia (Hz)');
% ylabel('Amplitud');
% 
% subplot(2,1,2);
% plot(wb, abs(B) / max(abs(B)));
% title('Señal submuestreada');
% xlabel('Frecuencia (Hz)');
% ylabel('Amplitud');

%

%%
%                           ######EJERCICIO 2########
%PA de dos polos

Fc = 8;
r=0.99;
titapa=2*pi*(Fc/Fsb);

b1=2*r*cos(titapa);
b2=r^2;
a1=-2;
a2=1;
Z = [1, a1, a2];             
P = [1,-b1, b2];             

% Filtrado de la señal PA
pa = filtfilt(Z, P, b);

% % Gráfica temporal de entrada y salida
% figure;
% plot(pa);
% title('Señal filtrada PA');
% xlabel('Tiempo (s)');
% ylabel('Amplitud');
% 
% % Diagrama de polos y ceros
% figure;
% zplane(Z, P);
% title('Diagrama de polos y ceros');
% 
% % Respuesta en frecuencia
% figure;
% freqz(Z, P, 1024, Fsb);
% title('Respuesta en frecuencia');

%

%%
% PB

ceros = [-1 -1]; % 
r = 0.92;
fc = 15; % Frecuencia de corte en 15Hz
titapb = fc*2*pi/Fsb; % Todo el círculo es Fsb = 600Hz
polos = [r.*exp(1j*titapb) r.*exp(1j*-titapb)]; 
num = poly(ceros);
den = poly(polos);
pb = filter(num,den,pa);

figure;
plot(pb);
title('Señal filtrada PA + PB');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% % Diagrama de polos y ceros
% figure;
% zplane(num, den);
% title('Diagrama de polos y ceros');
% 
% % Respuesta en frecuencia
% figure;
% freqz(den, num, 1024, Fsb);
% title('Respuesta en frecuencia');

%

%%
%Derivada de 5 puntos
h = (1/8)*[2 1 0 -1 -2];
der = conv(pb,h);
% figure;
% plot(der(1 : end - length(h)),'m');

%
%%
%Elevo al cuadrado
cuad=der.^2;
% figure;
% plot(cuad(1 : end - length(h)),'b');

%

%%
%Ventaneo

% Duración de la ventana en segundos
ventana = 0.08; % 80 milisegundos

% Convertir duración de la ventana a muestras
muestreo_ventana = round(ventana * Fsb);

% Crear la ventana rectangular
rectangular = ones(1, muestreo_ventana);

% Realizar la convolución
out_ventana = conv(cuad, rectangular, 'same');

% % Graficar la señal filtrada
% figure;
% plot(out_ventana);
% title('Señal Filtrada con Ventana Móvil');
% xlabel('Tiempo (s)');
% ylabel('Amplitud');


%

%%
% umbral
threshold = 2.6e9; % umbral
locs = [];
i = 1;
while i <= length(out_ventana)
    if out_ventana(i) > threshold
        locs = [locs, i]; % posición pico
        i = i + 200; % Saltar 200 muestras
    end
    i = i + 1;
end

% picos
pks = out_ventana(locs);
figure;
plot(out_ventana);
hold on;
plot(locs, pks, 'r^', 'MarkerFaceColor', 'r'); % Marcar los picos detectados
xlabel('Tiempo (s)');
ylabel('Amplitud');
title('QRS con Picos'); 
grid on;
hold off;

%
%%
%                            ######EJERCICIO 3########

%PA de dos polos

Fc_sm = 0.5;
r=0.99;
titapa_sm=2*pi*(Fc_sm/Fsb);

b1sm=2*r*cos(titapa_sm);
b2sm=r^2;
a1sm=-2;
a2sm=1;
Zsm = [1, a1sm, a2sm];             
Psm = [1,-b1sm, b2sm];             

% Filtrado de la señal PA
pa_sm = filtfilt(Zsm, Psm, b);

% Gráfica temporal de entrada y salida
figure;
plot(pa_sm);
title('Señal filtrada PA (del submuestreo)');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% % Diagrama de polos y ceros
% figure;
% zplane(Zsm, Psm);
% title('Diagrama de polos y ceros');
% 
% % Respuesta en frecuencia
% figure;
% freqz(Zsm, Psm, 1024, Fsb);
% title('Respuesta en frecuencia');

%

%%
%                            ######EJERCICIO 4########

% Filtro Notch (Peine)

fase1 = pi/5;
z1 = 1 .* exp(1j*fase1);
z2 = 1 .* exp(1j*-fase1);
fase2 = 3*pi/5;
z3 = 1 .* exp(1j*fase2);
z4 = 1 .* exp(1j*-fase2);
fase3 = pi;
z5 = 1 .* exp(1j*fase3);
z6 = 1 .* exp(1j*-fase3);
z_notch = [z1 z2 z3 z4 z5 z6];
ceros_notch = poly(z_notch);
polos_notch = [1 0 0 0 0 0];

% zplane(ceros_notch,polos_notch)
% grid
% freqz(ceros_notch, polos_notch, 2000, Fsb)

out_notch = filter(ceros_notch,polos_notch,pa_sm);

figure;
plot(out_notch,'k');
title('Notch');


%%
               %######EJERCICIO 5########
       %FSB=600hz
locs = floor(0.5.*([458, 1357, 2250, 3115, 4005, 4900, 5774, 6643, 7529, 8420, 9299, 10166, 11058, 11959, 12868, 13750, 14625, 15502, 16381, 17245, 18086, 18916, 19743, 20564, 21375, 22178, 22984, 23777, 24563, 25370, 26140, 26918, 27689, 28458, 29232, 30016, 30800, 31583, 32357, 33134, 33909, 34686, 35464, 36233]));

i=1;
salida=out_notch(locs(i)+60:locs(i)+60+150);
figure;
plot(salida)
grid on


for i = 2:length(locs)
    salida = salida + out_notch(locs(i)+60:locs(i)+60+150);
%     figure;
%     plot(salida);
    [maxim,posis]=max(salida);
    disp(maxim./length(locs))
end

salida_T=salida./length(locs); 
% figure;
plot(salida_T);  
grid on;
%


%%
%                 ##############EJERCICIO 6##############
[M,pos]=max(salida_T);
hold on;
stem(pos,M,'o');
title('Promedio señal T / máximo');
%
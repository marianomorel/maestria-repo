                                                  %EJE1%
% Datos de las columnas VG e ID
VG = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8];
ID1 = [-1.9763e-9, -1.1384e-9, 1.0156e-9, -2.0269e-9, -6.579e-10, 1.4791e-9, 2.7718e-9, 7.3839e-9, 3.6076e-8, 1.3365e-7, 4.069e-7, 9.8625e-7, 2.0127e-6, 3.4784e-6, 5.5149e-6, 8.1954e-6, 1.132e-5, 1.5126e-5, 1.9513e-5, 2.4673e-5, 3.0177e-5, 3.6297e-5, 4.3049e-5, 5.0315e-5, 5.8133e-5, 6.6733e-5, 7.5508e-5, 8.4619e-5, 9.4409e-5, 0.000104847, 0.00011516, 0.00012617, 0.00013752, 0.00014937, 0.00016153, 0.00017384, 0.00018608];
ID2 = [-1.1167e-009, 1.945e-010, -1.1061e-009, 2.4815e-009, 9.517e-010, -1.0466e-009, 2.3574e-009, 2.4465e-009, 9.107e-010, -4.848e-010, 3.4505e-009, 1.2978e-008, 5.5512e-008, 2.0667e-007, 5.9589e-007, 1.3378e-006, 2.5358e-006, 4.283e-006, 6.5901e-006, 9.5862e-006, 1.2944e-005, 1.7215e-005, 2.18e-005, 2.7108e-005, 3.3124e-005, 3.9577e-005, 4.6375e-005, 5.3898e-005, 6.1892e-005, 7.0633e-005, 7.9511e-005, 8.8693e-005, 9.8509e-005, 0.000108667, 0.00011928, 0.00013017, 0.00014158];
ID3 = [1.0605e-008, 1.0453e-008, 1.0296e-008, 1.0604e-008, 1.0578e-008, 1.0417e-008, 1.0323e-008, 1.0462e-008, 1.0576e-008, 1.0381e-008, 1.0329e-008, 1.0618e-008, 1.104e-008, 1.4237e-008, 2.9502e-008, 9.5081e-008, 3.0472e-007, 8.0617e-007, 1.6874e-006, 3.0772e-006, 5.0021e-006, 7.5064e-006, 1.05936e-005, 1.4356e-005, 1.8576e-005, 2.3539e-005, 2.8956e-005, 3.4853e-005, 4.1418e-005, 4.8553e-005, 5.6029e-005, 6.3927e-005, 7.2471e-005, 8.1448e-005, 9.0621e-005, 0.000100192, 0.000110346];

% Crear el gráfico
figure;
plot(VG, ID1, '-o', 'DisplayName', 'VBS = 0V');
hold on;
plot(VG, ID2, '-x', 'DisplayName', 'VBS = -0.9V'); 
plot(VG, ID3, '-*', 'DisplayName', 'VBS = -1.8V'); 
xlabel('VGS (volts)');
ylabel('ID (A)');
title('VGS vs ID');
grid on;
legend('show');

                                                   %EJE2%
% Crear el gráfico en escala semilogarítmica
figure;
semilogy(VG, abs(ID1), '-o', 'DisplayName', 'VBS = 0V');
hold on;
semilogy(VG, abs(ID2), '-x', 'DisplayName', 'VBS = -0.9V'); 
semilogy(VG, abs(ID3), '-*', 'DisplayName', 'VBS = -1.8V'); 
xlabel('VGS (V)');
ylabel('ID (A)');
title('VGS vs ID (Semilogarítmica)');
grid on;
legend('show');

                                                   %EJE3%
% Valores de V_D
VD = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8];
% Corrientes ID para diferentes VGS
ID_VGS_0 = [-1.1689e-009, 3.5e-011, -2.2424e-008, 2.086e-008, 5.544e-009, -1.4611e-008, -9.176e-009, 1.5462e-008, -2.2323e-008, 1.9828e-008, -4.438e-009, -2.1732e-008, 1.8098e-008, -4.849e-009, -2.1162e-008, -3.447e-009, 1.9585e-008, -4.487e-009, -2.1696e-008, 1.7755e-008, -4.959e-009, -2.1075e-008, -3.424e-009, 1.4777e-008, -4.53e-009, -2.1495e-008, -3.805e-009, 1.2985e-008, 5.633e-009, -1.4713e-008, -9.155e-009, 1.559e-008, -2.2276e-008, 1.9941e-008, 5.158e-009, -1.5731e-008, -8.768e-009];
ID_VGS_0_36 = [2.1455e-009, 1.2473e-008, 4.4592e-008, 3.4078e-008, 4.7866e-008, 4.6219e-008, 4.5481e-008, 4.7277e-008, 4.5198e-008, 4.8733e-008, 4.855e-008, 4.6833e-008, 4.6566e-008, 4.8842e-008, 4.9062e-008, 4.9124e-008, 4.9163e-008, 4.9125e-008, 4.7456e-008, 4.6785e-008, 5.0849e-008, 5.0178e-008, 5.0373e-008, 4.8863e-008, 4.7453e-008, 4.6767e-008, 5.0335e-008, 4.9975e-008, 5.0138e-008, 4.9073e-008, 4.7727e-008, 4.659e-008, 4.7581e-008, 5.0242e-008, 4.782e-008, 4.8041e-008, 4.7783e-008];
ID_VGS_0_72 = [1.2985e-008, 2.7719e-006, 4.6607e-006, 5.7633e-006, 6.2649e-006, 6.4372e-006, 6.4873e-006, 6.5082e-006, 6.5196e-006, 6.5276e-006, 6.535e-006, 6.5391e-006, 6.5496e-006, 6.5542e-006, 6.529e-006, 6.5331e-006, 6.5606e-006, 6.5294e-006, 6.5343e-006, 6.5405e-006, 6.5436e-006, 6.5483e-006, 6.5541e-006, 6.5575e-006, 6.5612e-006, 6.5652e-006, 6.5695e-006, 6.5723e-006, 6.5765e-006, 6.5802e-006, 6.5807e-006, 6.5871e-006, 6.59e-006, 6.5944e-006, 6.6003e-006, 6.6061e-006, 6.6111e-006];
ID_VGS_1_08 = [1.9309e-008, 8.0211e-006, 1.5134e-005, 2.1339e-005, 2.6596e-005, 3.0975e-005, 3.4487e-005, 3.708e-005, 3.8694e-005, 3.9627e-005, 3.9853e-005, 3.9922e-005, 4.0018e-005, 4.0002e-005, 4.0074e-005, 4.0068e-005, 4.0077e-005, 4.017e-005, 4.0096e-005, 4.0154e-005, 4.0143e-005, 4.0153e-005, 4.0236e-005, 4.0168e-005, 4.024e-005, 4.028e-005, 4.0372e-005, 4.0408e-005, 4.046e-005, 4.0269e-005, 4.0261e-005, 4.0335e-005, 4.0361e-005, 4.0449e-005, 4.0481e-005, 4.0527e-005, 4.0554e-005];
ID_VGS_1_44 = [3.2526e-008, 1.2499e-005, 2.4241e-005, 3.5228e-005, 4.543e-005, 5.4847e-005, 6.3454e-005, 7.1167e-005, 7.8092e-005, 8.4197e-005, 8.9401e-005, 9.3567e-005, 9.6946e-005, 9.9273e-005, 0.000100639, 0.000101543, 0.00010203, 0.000102295, 0.000102326, 0.000102435, 0.000102267, 0.000102194, 0.000102309, 0.000102417, 0.000102559, 0.000102572, 0.00010265, 0.000102452, 0.000102387, 0.000102486, 0.000102583, 0.000102717, 0.00010271, 0.00010247, 0.00010257, 0.000102496, 0.000102578];
ID_VGS_1_8 = [3.6891e-008, 1.5633e-005, 3.0748e-005, 4.5271e-005, 5.9224e-005, 7.2615e-005, 8.533e-005, 9.7426e-005, 0.000108899, 0.00011957, 0.00012948, 0.00013868, 0.00014713, 0.00015476, 0.00016153, 0.00016748, 0.00017252, 0.0001767, 0.00018004, 0.00018254, 0.00018418, 0.00018524, 0.00018545, 0.00018552, 0.00018554, 0.00018566, 0.00018567, 0.00018577, 0.00018581, 0.00018586, 0.00018587, 0.00018586, 0.00018596, 0.00018602, 0.000186, 0.00018604, 0.00018601];
% Crear la figura y plotear las curvas
figure;
hold on;
plot(VD, ID_VGS_0, '-o', 'DisplayName', 'V_{GS} = 0 V');
plot(VD, ID_VGS_0_36, '-*', 'DisplayName', 'V_{GS} = 0.36 V');
plot(VD, ID_VGS_0_72, '-s', 'DisplayName', 'V_{GS} = 0.72 V');
plot(VD, ID_VGS_1_08, '-d', 'DisplayName', 'V_{GS} = 1.08 V');
plot(VD, ID_VGS_1_44, '-^', 'DisplayName', 'V_{GS} = 1.44 V');
plot(VD, ID_VGS_1_8, '-v', 'DisplayName', 'V_{GS} = 1.8 V');
% Configuración de la gráfica
xlabel('V_D (V)');
ylabel('I_D (A)');
title('Curvas V_D vs I_D para diferentes valores de V_{GS}');
legend;
grid on;
hold off;

                                                %EJE4%
q=1.6e-19;
k=1.38e-23;
T=300;
VTH=k*T/q;
% Datos de las columnas VG e ID
ID1 = [-1.9763e-9, -1.1384e-9, 1.0156e-9, -2.0269e-9, -6.579e-10, 1.4791e-9, 2.7718e-9, 7.3839e-9, 3.6076e-8, 1.3365e-7, 4.069e-7, 9.8625e-7, 2.0127e-6, 3.4784e-6, 5.5149e-6, 8.1954e-6, 1.132e-5, 1.5126e-5, 1.9513e-5, 2.4673e-5, 3.0177e-5, 3.6297e-5, 4.3049e-5, 5.0315e-5, 5.8133e-5, 6.6733e-5, 7.5508e-5, 8.4619e-5, 9.4409e-5, 0.000104847, 0.00011516, 0.00012617, 0.00013752, 0.00014937, 0.00016153, 0.00017384, 0.00018608];
ID2 = [-1.1167e-009, 1.945e-010, -1.1061e-009, 2.4815e-009, 9.517e-010, -1.0466e-009, 2.3574e-009, 2.4465e-009, 9.107e-010, -4.848e-010, 3.4505e-009, 1.2978e-008, 5.5512e-008, 2.0667e-007, 5.9589e-007, 1.3378e-006, 2.5358e-006, 4.283e-006, 6.5901e-006, 9.5862e-006, 1.2944e-005, 1.7215e-005, 2.18e-005, 2.7108e-005, 3.3124e-005, 3.9577e-005, 4.6375e-005, 5.3898e-005, 6.1892e-005, 7.0633e-005, 7.9511e-005, 8.8693e-005, 9.8509e-005, 0.000108667, 0.00011928, 0.00013017, 0.00014158];
ID3 = [1.0605e-008, 1.0453e-008, 1.0296e-008, 1.0604e-008, 1.0578e-008, 1.0417e-008, 1.0323e-008, 1.0462e-008, 1.0576e-008, 1.0381e-008, 1.0329e-008, 1.0618e-008, 1.104e-008, 1.4237e-008, 2.9502e-008, 9.5081e-008, 3.0472e-007, 8.0617e-007, 1.6874e-006, 3.0772e-006, 5.0021e-006, 7.5064e-006, 1.05936e-005, 1.4356e-005, 1.8576e-005, 2.3539e-005, 2.8956e-005, 3.4853e-005, 4.1418e-005, 4.8553e-005, 5.6029e-005, 6.3927e-005, 7.2471e-005, 8.1448e-005, 9.0621e-005, 0.000100192, 0.000110346];
% Crear el gráfico en escala semilogarítmica
figure;
semilogy(VG, abs(ID1), '-o', 'DisplayName', 'VBS = 0V');
hold on;
semilogy(VG, abs(ID2), '-x', 'DisplayName', 'VBS = -0.9V'); 
semilogy(VG, abs(ID3), '-*', 'DisplayName', 'VBS = -1.8V'); 
xlabel('VGS (V)');
ylabel('ID (A)');
title('VGS vs ID (Semilogarítmica)');
grid on;

% fit_1
% Obtener los índices de los puntos en el rango de VG de 0.35 a 0.5
indice_inicio1 = find(VG == 0.35);
indice_fin1 = find(VG == 0.5);
% Realizar la regresión lineal para ID1 entre VG de 0.35 y 0.5
x1 = VG(indice_inicio1:indice_fin1); % valores de VG entre 0.35 y 0.5
y1 = abs(ID1(indice_inicio1:indice_fin1)); % valores correspondientes de ID1
p1 = polyfit(x1, log(y1), 1); % realizar regresión lineal en escala semilogarítmica
y_fit1 = exp(polyval(p1, VG(indice_inicio1:indice_fin1))); % calcular valores ajustados
% Agregar la línea punteada de regresión lineal al gráfico
semilogy(VG(indice_inicio1:indice_fin1), y_fit1, '--k', 'LineWidth', 2, 'DisplayName', 'Regresión Lineal (VBS=0V)');
legend('show');
ID1_MIN = exp(polyval(p1, 0.35));
ID1_MAX = exp(polyval(p1, 0.5));

% fit_2
% Obtener los índices de los puntos en el rango de VG de 0.5 a 0.65
indice_inicio2 = find(VG == 0.5);
indice_fin2 = find(VG == 0.65);
% Realizar la regresión lineal para ID2 entre VG de 0.5 y 0.65
x2 = VG(indice_inicio2:indice_fin2); % valores de VG entre 0.5 y 0.65
y2 = abs(ID2(indice_inicio2:indice_fin2)); % valores correspondientes de ID2
p2 = polyfit(x2, log(y2), 1); % realizar regresión lineal en escala semilogarítmica
y_fit2 = exp(polyval(p2, VG(indice_inicio2:indice_fin2))); % calcular valores ajustados
% Agregar la línea punteada de regresión lineal al gráfico
semilogy(VG(indice_inicio2:indice_fin2), y_fit2, '--k', 'LineWidth', 2, 'DisplayName', 'Regresión Lineal (VBS=-0.9V)');
legend('show');
ID2_MIN = exp(polyval(p2, 0.5));
ID2_MAX = exp(polyval(p2, 0.65));

% fit_3
% Obtener los índices de los puntos en el rango de VG de 0.7 y 0.85
indice_inicio3 = find(VG == 0.7);
indice_fin3 = find(VG == 0.85);
% Realizar la regresión lineal para ID3 entre VG de 0.7 y 0.85
x3 = VG(indice_inicio3:indice_fin3); % valores de VG entre 0.7 y 0.85
y3 = abs(ID3(indice_inicio3:indice_fin3)); % valores correspondientes de ID3
p3 = polyfit(x3, log(y3), 1); % realizar regresión lineal en escala semilogarítmica
y_fit3 = exp(polyval(p3, VG(indice_inicio3:indice_fin3))); % calcular valores ajustados
% Agregar la línea punteada de regresión lineal al gráfico
semilogy(VG(indice_inicio3:indice_fin3), y_fit3, '--k', 'LineWidth', 2, 'DisplayName', 'Regresión Lineal (VBS=-1.8V)');
legend('show');
ID3_MIN = exp(polyval(p3, 0.7));
ID3_MAX = exp(polyval(p3, 0.85));

%S1 = (0.5-0.35) / ((log(ID1_MAX) - log(ID1_MIN)) / log(10));
%S2 = (0.65-0.5) / ((log(ID2_MAX) - log(ID2_MIN)) / log(10));
%S3 = (0.85-0.7) / ((log(ID3_MAX) - log(ID3_MIN)) / log(10));

S=[(0.5-0.35) / ((log(ID1_MAX) - log(ID1_MIN)) / log(10)),(0.65-0.5) / ((log(ID2_MAX) - log(ID2_MIN)) / log(10)),(0.85-0.7) / ((log(ID3_MAX) - log(ID3_MIN)) / log(10))];

%m1 = S1 / (2.3 * VTH);
%m2 = S2 / (2.3 * VTH);
%m3 = S3 / (2.3 * VTH);

m = [S(1) / (2.3 * VTH), S(2) / (2.3 * VTH), S(3) / (2.3 * VTH)];

                                             %eje5%
%con la ecuacion de saturacion dada%
% Datos proporcionados
ID1 = [-1.9763e-9, -1.1384e-9, 1.0156e-9, -2.0269e-9, -6.579e-10, 1.4791e-9, 2.7718e-9, 7.3839e-9, 3.6076e-8, 1.3365e-7, 4.069e-7, 9.8625e-7, 2.0127e-6, 3.4784e-6, 5.5149e-6, 8.1954e-6, 1.132e-5, 1.5126e-5, 1.9513e-5, 2.4673e-5, 3.0177e-5, 3.6297e-5, 4.3049e-5, 5.0315e-5, 5.8133e-5, 6.6733e-5, 7.5508e-5, 8.4619e-5, 9.4409e-5, 0.000104847, 0.00011516, 0.00012617, 0.00013752, 0.00014937, 0.00016153, 0.00017384, 0.00018608];
ID2 = [-1.1167e-009, 1.945e-010, -1.1061e-009, 2.4815e-009, 9.517e-010, -1.0466e-009, 2.3574e-009, 2.4465e-009, 9.107e-010, -4.848e-010, 3.4505e-009, 1.2978e-008, 5.5512e-008, 2.0667e-007, 5.9589e-007, 1.3378e-006, 2.5358e-006, 4.283e-006, 6.5901e-006, 9.5862e-006, 1.2944e-005, 1.7215e-005, 2.18e-005, 2.7108e-005, 3.3124e-005, 3.9577e-005, 4.6375e-005, 5.3898e-005, 6.1892e-005, 7.0633e-005, 7.9511e-005, 8.8693e-005, 9.8509e-005, 0.000108667, 0.00011928, 0.00013017, 0.00014158];
ID3 = [1.0605e-008, 1.0453e-008, 1.0296e-008, 1.0604e-008, 1.0578e-008, 1.0417e-008, 1.0323e-008, 1.0462e-008, 1.0576e-008, 1.0381e-008, 1.0329e-008, 1.0618e-008, 1.104e-008, 1.4237e-008, 2.9502e-008, 9.5081e-008, 3.0472e-007, 8.0617e-007, 1.6874e-006, 3.0772e-006, 5.0021e-006, 7.5064e-006, 1.05936e-005, 1.4356e-005, 1.8576e-005, 2.3539e-005, 2.8956e-005, 3.4853e-005, 4.1418e-005, 4.8553e-005, 5.6029e-005, 6.3927e-005, 7.2471e-005, 8.1448e-005, 9.0621e-005, 0.000100192, 0.000110346];

% Filtrar los datos a partir de las muestras especificadas
VG1 = VG(VG >= 0.65);
ID1_filtered = ID1(VG >= 0.65);

VG2 = VG(VG >= 0.8);
ID2_filtered = ID2(VG >= 0.8);

VG3 = VG(VG >= 0.9);
ID3_filtered = ID3(VG >= 0.9);

% Ajuste polinómico de segundo grado para ID1 a partir de 0.65
pc1 = polyfit(VG1, ID1_filtered, 2);
VG_fit1 = linspace(min(VG1), max(VG1), 500);
ID1_fit = polyval(pc1, VG_fit1);

% Ajuste polinómico de segundo grado para ID2 a partir de 0.8
pc2 = polyfit(VG2, ID2_filtered, 2);
VG_fit2 = linspace(min(VG2), max(VG2), 500);
ID2_fit = polyval(pc2, VG_fit2);

% Ajuste polinómico de segundo grado para ID3 a partir de 0.9
pc3 = polyfit(VG3, ID3_filtered, 2);
VG_fit3 = linspace(min(VG3), max(VG3), 500);
ID3_fit = polyval(pc3, VG_fit3);

% Graficar los datos originales y el ajuste para ID1, ID2 e ID3 en un mismo gráfico
figure;
plot(VG, ID1, 'bo', 'DisplayName', 'Datos originales ID1 VBS = 0V');
hold on;
plot(VG_fit1, ID1_fit, 'b-', 'DisplayName', 'Ajuste cuadrático ID1');
plot(VG, ID2, 'go', 'DisplayName', 'Datos originales ID2 VBS = -0.9V');
plot(VG_fit2, ID2_fit, 'g-', 'DisplayName', 'Ajuste cuadrático ID2');
plot(VG, ID3, 'mo', 'DisplayName', 'Datos originales ID3 VBS = -1.8V');
plot(VG_fit3, ID3_fit, 'm-', 'DisplayName', 'Ajuste cuadrático ID3');
xlabel('VG');
ylabel('ID');
title('Ajuste Cuadrático a los Datos ID1, ID2 e ID3');
legend('show');
grid on;
hold off;

% Mostrar los coeficientes de los polinomios ajustados
disp('Coeficientes del polinomio cuadrático ajustado para ID1: ');
disp(pc1);
disp('Coeficientes del polinomio cuadrático ajustado para ID2: ');
disp(pc2);
disp('Coeficientes del polinomio cuadrático ajustado para ID3: ');
disp(pc3);

%valores de Kn y VT calculados a mano%
%VT=0.406V ; Kn=2.863E-04
%VT=0.612V ; Kn=2.885E-04
%VT=0.764V ; Kn=3.639E-04


                                           %eje6%
% Crear la figura y plotear las curvas
figure;
hold on;
plot(VD, ID_VGS_0, '-o', 'DisplayName', 'V_{GS} = 0 V');
plot(VD, ID_VGS_0_36, '-*', 'DisplayName', 'V_{GS} = 0.36 V');
plot(VD, ID_VGS_0_72, '-s', 'DisplayName', 'V_{GS} = 0.72 V');
plot(VD, ID_VGS_1_08, '-d', 'DisplayName', 'V_{GS} = 1.08 V');
plot(VD, ID_VGS_1_44, '-^', 'DisplayName', 'V_{GS} = 1.44 V');
plot(VD, ID_VGS_1_8, '-v', 'DisplayName', 'V_{GS} = 1.8 V');
% Configuración de la gráfica
xlabel('V_D (V)');
ylabel('I_D (A)');
title('Curvas V_D vs I_D para diferentes valores de V_{GS}');
legend;
grid on;
% Calcular y marcar el primer punto donde la derivada es cercana a cero
threshold = 1e-5; % Umbral para considerar la derivada cercana a cero
curves = {ID_VGS_0, ID_VGS_0_36, ID_VGS_0_72, ID_VGS_1_08, ID_VGS_1_44, ID_VGS_1_8};
VGS_values = {'0 V', '0.36 V', '0.72 V', '1.08 V', '1.44 V', '1.8 V'};
markers = {'o', '*', 's', 'd', '^', 'v'};
VDS_SAT = []; % Vector para almacenar los valores de V_DS en saturación

for i = 1:length(curves)
    ID = curves{i};
    dID_dVD = diff(ID) ./ diff(VD); % Calcular la derivada
    idx = find(abs(dID_dVD) < threshold, 1); % Encontrar el primer índice donde la derivada es menor al umbral
    if ~isempty(idx)
        VDS_SAT = [VDS_SAT, VD(idx)]; % Agregar el valor de V_DS en saturación al vector
        plot(VD(idx), ID(idx), 'ko', 'MarkerFaceColor', 'k', 'DisplayName', sprintf('V_{GS} = %s, V_{DS} = %.2f V', VGS_values{i}, VD(idx)));
    end
end

hold off;

% Mostrar los valores de VDS_SAT
%disp('Valores de VDS_SAT:');
%disp(VDS_SAT);
% Crear la figura y plotear las curvas
figure;
hold on;
plot(VD, ID_VGS_0, '-o', 'DisplayName', 'V_{GS} = 0 V');
plot(VD, ID_VGS_0_36, '-*', 'DisplayName', 'V_{GS} = 0.36 V');
plot(VD, ID_VGS_0_72, '-s', 'DisplayName', 'V_{GS} = 0.72 V');
plot(VD, ID_VGS_1_08, '-d', 'DisplayName', 'V_{GS} = 1.08 V');
plot(VD, ID_VGS_1_44, '-^', 'DisplayName', 'V_{GS} = 1.44 V');
plot(VD, ID_VGS_1_8, '-v', 'DisplayName', 'V_{GS} = 1.8 V');
% Configuración de la gráfica
xlabel('V_D (V)');
ylabel('I_D (A)');
title('Curvas V_D vs I_D para diferentes valores de V_{GS}');
legend;
grid on;
% Calcular y marcar el primer punto donde la derivada es cercana a cero
threshold = 1e-5; % Umbral para considerar la derivada cercana a cero
curves = {ID_VGS_0, ID_VGS_0_36, ID_VGS_0_72, ID_VGS_1_08, ID_VGS_1_44, ID_VGS_1_8};
VGS_values = {'0 V', '0.36 V', '0.72 V', '1.08 V', '1.44 V', '1.8 V'};
markers = {'o', '*', 's', 'd', '^', 'v'};
% Estimación y plot de VA para cada curva
VA_values = zeros(1, length(curves));

for i = 1:length(curves)
    ID = curves{i};
    dID_dVD = diff(ID) ./ diff(VD); % Calcular la derivada
    idx = find(abs(dID_dVD) < threshold, 1); % Encontrar el primer índice donde la derivada es menor al umbral
    if ~isempty(idx)
        % Selección de la región de saturación
        saturation_region = idx:length(VD);
        VD_sat = VD(saturation_region);
        ID_sat = ID(saturation_region);
        
        % Realizar la regresión lineal
        p = polyfit(VD_sat, ID_sat, 1);
        slope = p(1);
        intercept = p(2);
        
        % Calcular la intersección con el eje VD (VA)
        VA = -intercept / slope;
        VA_values(i) = VA;
        
        % Mostrar el valor de VA para esta curva en un recuadro
        annotation('textbox', [0.65 0.85-(i-1)*0.1 0.2 0.1], 'String', sprintf('V_{GS} = %s\nVA = %.2f V', VGS_values{i}, VA), 'FitBoxToText', 'on', 'EdgeColor', 'none');
        
        % Mostrar el valor de VA para esta curva
        % fprintf('V_{GS} = %s, VA = %.2f V\n', VGS_values{i}, VA);
    end
end

hold off; 

%EJE7 (de la ecuacion)%                   %esto es con ecuacion%
% Definir los parámetros conocidos
%gamma = 0.746;      % Constante gamma
%psi_B = -0.399;     % Potencial de banda
%VT0 = 0.555;        % Voltaje umbral inicial
% Definir valores de VBS
%VBS = [0, -0.9, -1.8];   % Voltaje bulk-source
% Calcular VT para cada valor de VBS
%VT = VT0 + gamma * (sqrt(-VBS - 2 * psi_B) - sqrt(-2 * psi_B));
% Mostrar los resultados
%disp('Valores de VT:');
%disp(VT);
% Graficar VT vs VBS
%figure;
%plot(VBS, VT, 'o-', 'LineWidth', 2, 'MarkerSize', 8);
%grid on;
%xlabel('V_{BS}');
%ylabel('V_{T}');
%title('Gráfico de V_{T} vs V_{BS}');
%Valores de VT:
%    0.5550    0.8607    1.0910

%EJE8 (de la ecuacion)%                      %esto es con ecuacion%
% Definir los parámetros conocidos
%gamma = 0.746;      % Constante gamma
%psi_B = -0.399;     % Potencial de banda
%VBS = [0, -0.9, -1.8];   % Voltaje bulk-source
% Calcular m(VBS)
%m_VBS = 1 + (gamma ./ (2 .* sqrt(-VBS - 2 .* psi_B)));
% Mostrar el resultado
%disp('Valores de m(VBS):');
%disp(m_VBS);
% Graficar m(VBS) vs VBS
%figure;
%plot(VBS, m_VBS, 'o-', 'LineWidth', 2, 'MarkerSize', 8);
%grid on;
%xlabel('V_{BS}');
%ylabel('m(V_{BS})');
%title('Gráfico de m(V_{BS}) vs V_{BS}');

                      %eje7%
% Datos proporcionados
VT = [0.406, 0.612, 0.764];   % Voltaje umbral VT en voltios
VBS = [0, -0.9, -1.8];        % Voltaje bulk-source VBS en voltios
% Graficar VT vs VBS
figure;
plot(VBS, VT, 'o-', 'LineWidth', 2, 'MarkerSize', 8);
grid on;
xlabel('V_{BS} (V)');
ylabel('V_{T} (V)');
title('V_{T} vs V_{BS}');

                      %eje8%
% Datos proporcionados
% Graficar m(VBS) vs VBS
figure;
plot(VBS, m, 'o-', 'LineWidth', 2, 'MarkerSize', 8);
grid on;
xlabel('V_{BS} (V)');
ylabel('m(V_{BS})');
title('m vs V_{BS}');

                      %eje9%
% Datos proporcionados
Kn = [2.863E-04, 2.885E-04, 3.639E-04]; % Valores de Kn
% Graficar Kn vs VBS
figure;
plot(VBS, Kn, 'o-', 'LineWidth', 2, 'MarkerSize', 8);
grid on;
xlabel('V_{BS} (V)');
ylabel('K_{n}');
title('K_{n} vs V_{BS}');

                     %eje10%

% Curvas de corriente ID para diferentes VGS
ID_curves = {ID_VGS_0, ID_VGS_0_36, ID_VGS_0_72, ID_VGS_1_08, ID_VGS_1_44, ID_VGS_1_8};
VGS_labels = {'0V', '0.36V', '0.72V', '1.08V', '1.44V', '1.8V'};

% Rango de índices para calcular la media
% Aquí se podría ajustar según el punto donde consideres que la curva se estabiliza
inicio_indice_estable = 15;  % Ajustar según la observación de las curvas
fin_indice_estable = length(VD);  % Puedes ajustar este valor según sea necesario

% Calcular la corriente de saturación como el promedio de los valores en el rango establecido
I_saturation = zeros(size(ID_curves));

for i = 1:length(ID_curves)
    ID_curve = ID_curves{i};
    ID_stable_range = ID_curve(inicio_indice_estable:fin_indice_estable);
    I_saturation(i) = mean(ID_stable_range);
end

% Mostrar los valores de corriente de saturación
%fprintf('Corriente de saturación promedio para cada curva:\n');
%for i = 1:length(I_saturation)
 %   fprintf('VGS = %s: %.4e A\n', VGS_labels{i}, I_saturation(i));
%end

% Graficar
figure;
plot(VA_values, I_saturation, '-o', 'LineWidth', 1.5);
xlabel('VA Values');
ylabel('ID SAT (A)');
title('ID SAT vs VA');
grid on;
grid minor;

%no se mantiene constante%

                         %EJE11%
% Datos proporcionados
VGS_SAT = [0, 0.36, 0.72, 1.08, 1.44, 1.8];
% Calcular VDS_SAT_CALC
VDS_SAT_CALC = (VGS_SAT - VT(1)) / m(1);
% Redondear los valores negativos a 0
VDS_SAT_CALC(VDS_SAT_CALC < 0) = 0;

% Mostrar los resultados
%disp('Valores calculados de VDS_SAT_CALC:');
%disp(VDS_SAT_CALC);

% Calcular la diferencia absoluta
diferencia_absoluta = abs(VDS_SAT - VDS_SAT_CALC);

% Crear una tabla
T = table(VDS_SAT', VDS_SAT_CALC', diferencia_absoluta', ...
    'VariableNames', {'VDS_estimado', 'VDS_calculado', 'Diferencia_absoluta'});

% Mostrar la tabla
disp('Tabla de comparación entre VDS_estimado y VDS_calculado:');
disp(T);

                                  %EJE12%
ID01 = [-5.151e-010, 2.3954e-009, 1.7275e-009, -1.7824e-009, -9.114e-010, 1.7949e-009, 2.0516e-009, 6.3392e-009, 3.2233e-008, 1.2733e-007, 3.7477e-007, 9.1276e-007, 1.7342e-006, 2.8258e-006, 4.113e-006, 5.5353e-006, 6.9834e-006, 8.421e-006, 9.9105e-006, 1.1392e-005, 1.2879e-005, 1.4297e-005, 1.5724e-005, 1.7104e-005, 1.8484e-005, 1.977e-005, 2.1001e-005, 2.2214e-005, 2.3365e-005, 2.4506e-005, 2.5524e-005, 2.6548e-005, 2.7495e-005, 2.8372e-005, 2.9218e-005, 3.0006e-005, 3.0755e-005];
ID18 = [-1.9763e-009, -1.1384e-009, 1.0156e-009, -2.0269e-009, -6.579e-010, 1.4791e-009, 2.7718e-009, 7.3839e-009, 3.6076e-008, 1.3365e-007, 4.069e-007, 9.8625e-007, 2.0127e-006, 3.4784e-006, 5.5149e-006, 8.1954e-006, 1.132e-005, 1.5126e-005, 1.9513e-005, 2.4673e-005, 3.0177e-005, 3.6297e-005, 4.3049e-005, 5.0315e-005, 5.8133e-005, 6.6733e-005, 7.5508e-005, 8.4619e-005, 9.4409e-005, 0.000104847, 0.00011516, 0.00012617, 0.00013752, 0.00014937, 0.00016153, 0.00017384, 0.00018608];

% Valores de VDS
VDS = [0.1,1.8];

% Prealocar matriz de salida para ID_S
ID_S = zeros(length(VDS), length(VG)); 

% Calcular ID_S por tramos para cada valor de VDS
for j = 1:length(VDS)
    for i = 1:length(VG)
        if VG(i) > VT(1) && VDS(j) < VDS_SAT(6)
            ID_S(j, i) = Kn(1) * (VG(i) - VT(1) - m(1)/2 * VDS(j)) * VDS(j);
        elseif VG(i) > VT(1) && VDS(j) >= VDS_SAT(6)
            ID_S(j, i) = Kn(1) * ((VG(i) - VT(1))^2) / (2 * m(1));
        elseif VG(i) <= VT(1)
            ID_S(j, i) = Kn(1) * (m(1) - 1) * VTH^2 * exp((VG(i) - VT(1)) / (m(1) * VTH)) * (1 - exp(-VDS(j) / VTH));
        end
    end
end

% Crear la gráfica combinada
figure;
hold on;
plot(VG, ID01, 'b-o', 'DisplayName', 'ID01');
plot(VG, ID18, 'r-o', 'DisplayName', 'ID18');

for j = 1:length(VDS)
    plot(VG, ID_S(j, :), 'LineWidth', 2, 'DisplayName', ['VDS = ' num2str(VDS(j)) ' V']);
end

% Etiquetas y título
xlabel('VG (V)');
ylabel('ID (A)');
title('ID vs. VG para diferentes curvas');
legend('show');
grid on;
hold off;

%USE VDS_SAT = 1.05


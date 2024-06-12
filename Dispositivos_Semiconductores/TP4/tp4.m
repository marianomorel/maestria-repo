%eje1%

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
title('Gráfico de VGS vs ID');
grid on;
legend('show');

%eje2%

% Crear el gráfico en escala semilogarítmica
figure;
semilogy(VG, abs(ID1), '-o', 'DisplayName', 'VBS = 0V');
hold on;
semilogy(VG, abs(ID2), '-x', 'DisplayName', 'VBS = -0.9V'); 
semilogy(VG, abs(ID3), '-*', 'DisplayName', 'VBS = -1.8V'); 
xlabel('VGS (V)');
ylabel('ID (A)');
title('Gráfico de VGS vs ID (Escala Semilogarítmica)');
grid on;
legend('show');

%eje3%

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

%eje4%

q=1.6e-19;
k=1.38e-23;
T=300;
VTH=k*T/q;

% Datos de las columnas VG e ID
VG = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8];
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
title('Gráfico de VGS vs ID (Escala Semilogarítmica)');
grid on;

%fit_1%

% Obtener los índices de los puntos en el rango de VG de 0.35 a 0.5
indice_inicio1 = find(VG == 0.35);
indice_fin1 = find(VG == 0.5);

% Realizar la regresión lineal para ID1 entre VG de 0.35 y 0.5
x1 = VG(indice_inicio1:indice_fin1); % valores de VG entre 0.35 y 0.5
y1 = abs(ID1(indice_inicio1:indice_fin1)); % valores correspondientes de ID1
p1 = polyfit(x1, log(y1), 1); % realizar regresión lineal en escala semilogarítmica
y_fit1 = exp(polyval(p1, VG(indice_inicio1:indice_fin1))); % calcular valores ajustados

% Agregar la línea punteada de regresión lineal al gráfico
semilogy(VG(indice_inicio1:indice_fin1), y_fit1, '--', 'DisplayName', 'Regresión Lineal (VBS=0V)');
legend('show');

%fit_2%

% Obtener los índices de los puntos en el rango de VG de 0.5 a 0.65
indice_inicio2 = find(VG == 0.5);
indice_fin2 = find(VG == 0.65);

% Realizar la regresión lineal para ID1 entre VG de 0.5 y 0.65
x2 = VG(indice_inicio2:indice_fin2); % valores de VG entre 0.5 y 0.65
y2 = abs(ID2(indice_inicio2:indice_fin2)); % valores correspondientes de ID2
p2 = polyfit(x2, log(y2), 1); % realizar regresión lineal en escala semilogarítmica
y_fit2 = exp(polyval(p2, VG(indice_inicio2:indice_fin2))); % calcular valores ajustados

% Agregar la línea punteada de regresión lineal al gráfico
semilogy(VG(indice_inicio2:indice_fin2), y_fit2, '--', 'DisplayName', 'Regresión Lineal (VBS=-0.9V)');
legend('show');

%fit_3%

% Obtener los índices de los puntos en el rango de VG de 0.7 y 0.85
indice_inicio3 = find(VG == 0.7);
indice_fin3 = find(VG == 0.85);

% Realizar la regresión lineal para ID1 entre VG de 0.7 y 0.85
x3 = VG(indice_inicio3:indice_fin3); % valores de VG entre 0.7 y 0.85
y3 = abs(ID3(indice_inicio3:indice_fin3)); % valores correspondientes de ID3
p3 = polyfit(x3, log(y3), 1); % realizar regresión lineal en escala semilogarítmica
y_fit3 = exp(polyval(p3, VG(indice_inicio3:indice_fin3))); % calcular valores ajustados

% Agregar la línea punteada de regresión lineal al gráfico
semilogy(VG(indice_inicio3:indice_fin3), y_fit3, '--', 'DisplayName', 'Regresión Lineal (VBS=-1.8V)');
legend('show');

% Pendiente de la regresión lineal para ID1 (VBS=0V)
S1 = p1(1);

% Pendiente de la regresión lineal para ID2 (VBS=-0.9V)
S2 = p2(1);

% Pendiente de la regresión lineal para ID3 (VBS=-1.8V)
S3 = p3(1);

disp(['La pendiente de la regresión lineal para ID1 es: ', num2str(S1)]);
disp(['La pendiente de la regresión lineal para ID2 es: ', num2str(S2)]);
disp(['La pendiente de la regresión lineal para ID3 es: ', num2str(S3)]);

S1=1/S1;
S2=1/S2;
S3=1/S3;

m1=S1/(2.3*VTH);
m2=S2/(2.3*VTH);
m3=S3/(2.3*VTH);

%m no puede ser menor que la unidad%

%eje5%
%con la ecuacion de saturacion dada%
% Datos proporcionados
VG = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8];
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

%VT=0.406V ; Kn=1.243E-04
%VT=0.612V ; Kn=1.253E-04
%VT=0.764V ; Kn=1.580E-04

% Promediado de se?ales% Modelo
Fs = 1000;
f = 1;
n = 0 : 1/Fs : 0.499;
y = [sin(2*pi*f*n) zeros(1,500)];
m = 1000;
signal = zeros(1,m*length(y));
for i = 1 : m 
    signal((i-1)*length(y)+1:i*length(y)) = y;
end
signal = signal + 1.*randn(1,length(signal));
plot(signal,'LineWidth',2)
L = 500;
marcas = 1 : 500 : m*length(y);
vector = zeros(1,L);
for i = 1 : m 
    vector = vector + signal((i-1)*L+1:i*L);
end
vector = vector / m;
figure
plot(vector);
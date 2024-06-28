function[X, w]=fourierseries(x,T0,N)

% Funcion fourierseries
% computa analiticamente arm�nicos de la serie de fourier de se�ales continuas 
% input: se�al periodica x(t), periodo (T0), numero de armonicos (N)
% output: armonicos X, frecuencias w

syms t

for k=1:N,
    
X1(k)=int(x*exp(-j*2*pi*(k-1)*t/T0),t,0,T0)/T0;

X(k)=subs(X1(k));

w(k)=(k-1)*2*pi/T0;

end

end
   
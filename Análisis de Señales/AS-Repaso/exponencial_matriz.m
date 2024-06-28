fi0=ones(1,length(f));
fi1=[0:length(f)-1];

A=[fi0*fi0',fi0*fi1';fi1*fi0',fi1*fi1'];
B=[log(f)*fi0';log(f)*fi1'];

syms x t

x=A\B;
f2=fit(n',f','exp1');
b0=f2.a;
b1=f2.b;
plot(f)
hold on
plot(exp(x(1))*exp(x(2)*n))
plot(b0*exp(b1*n))

clear all; 
clf
t=0:0.01:20;
n=0:20;
x1=(0.8).^n; 
x2=(0.8).^t;
figure(1)
hold on;
stem(n,x1); 
plot(t,x2)
grid
hold off;

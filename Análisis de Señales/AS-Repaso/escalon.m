function y=escalon(t,ad)
% generation of unit step
% t: time
% ad : advance (positive), delay (negative)
% USE y=unitstep(t,ad)
N=length(t);
y=zeros(1,N);
for i=1:N,
if t(i)>=-ad,
y(i)=1;
end
end

%EJEMPLO
%clear all;
%clf;
%Ts=0.01;
%t=-5:Ts:5;
%y1=ramp(t,3,3);
%y2=unistep(t,-3);
%y=y1+y2;
%plot(t,y,'r');
%axis([- 5 5 -1 7])
%grid;
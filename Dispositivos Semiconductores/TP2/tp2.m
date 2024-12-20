na=2*10^14; %EJE1
nd=1*10^15;
wn=30*10^-6;
wp=30*10^-6;
tmin=1*10^-6;
tmax=100*10^-6;
vapp=300*10^-3;
wp=30*10^-6;
T=27+273.15;
q=1.6*10^-19;
m0=9.11*10^-31;
k=1.38e-23;
%unmin=tmin*q/(0.26*m0);
%unmax=tmax*q/(0.26*m0);
%upmin=tmin*q/(0.38*m0);
%upmax=tmax*q/(0.38*m0);
%Dnmin=k*unmin*T/q;
%Dnmax=k*unmax*T/q;
%Dpmin=k*upmin*T/q;
%Dpmax=k*upmax*T/q;
%lnmin=(Dnmin*tmin)^0.5;
%lnmax=(Dnmax*tmax)^0.5;
%lpmin=(Dpmin*tmin)^0.5;
%lpmax=(Dpmax*tmax)^0.5;
esi = 11.7*8.85e-12;
Nc=2.9e19;
Nv=3.1e19;
eg=1.12;
k1=8.617e-5;

ni=((Nc*Nv)^0.5)*exp(-eg/(2*k1*T)); %EJE2 %cm-3
fibi=(k*T/q)*log(na*nd/ni^2);
wd=((2*esi*(na+nd)*fibi*0.01^3)/(q*na*nd))^0.5;
em=fibi*2/wd;
xn=em*esi/(q*nd);
xn=xn*(0.01)^3;
xp=wd-xn;

fim=fibi-vapp; %EJE3
wdvapp=((2*esi*(na+nd)*fim*0.01^3)/(q*na*nd))^0.5;
emvapp=fim*2/wdvapp;
xnvapp=emvapp*esi/(q*nd);
xnvapp=xnvapp*(0.01)^3;
xpvapp=wdvapp-xnvapp;

j0=q*(ni^2)*(Dnmax/(wp*na)+Dpmax/((wn-wdvapp)*nd)); %EJE4
j0=j0/(0.01)^3;
vth=0.026;
j=-j0*(exp(vapp/vth)-1);
jn=-q*(ni^2)*(Dnmax/(wp*na))*(exp(vapp/vth)-1);
jp=-q*(ni^2)*(Dpmax/((wn-wdvapp)*nd))*(exp(vapp/vth)-1);
jn=jn/(0.01^3);
jp=jp/(0.01^3);
nporc=100*jn/j;
pporc=100*jp/j;

fim=xp*em/2; %EJE5
no=ni*exp(-q*fim/(k*T));
po=(ni^2)/no;
janxp=q*unnd*po*em/(0.01)^3;
japxp=q*upna*no*em/(0.01)^3;

nxp=nd*exp(-fim/(k*T/q)); %EJE6
pxn=na*exp(-fim/(k*T/q));
nxpbni=((ni^2)/na)*exp(vapp/vth);
pxnbni=((ni^2)/nd)*exp(vapp/vth);

minnp=((ni^2)/na)*(exp(vapp/vth)-1)*(1-x/wp); %EJE7
minpn=((ni^2)/nd)*(exp(vapp/vth)-1)*(1+(x+wd)/(wn-wd));
jnd=-(q*Dnnd*diff(minnp))/(0.01^3);
jpd=(q*Dnna*diff(minpn))/(0.01^3);

%EJE 8 es una resta

emap=(0.394*(0.01)^3)/(q*upna*na); %EJE9
eman=(2.684*(0.01)^3)/(q*unnd*nd);
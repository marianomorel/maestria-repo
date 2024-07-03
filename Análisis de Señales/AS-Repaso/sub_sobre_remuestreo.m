%Fs=
F=fft(abs(f));
L=length(F);
w=0:2*pi/L:2*pi-2*pi/L;

for i=1:4 %esto no es necesario si conocemos el submuestreo que queremos hacer
    b=downsample(y,2^i);
    B=fft(abs(b));
end

subplot(2,1,1);
plot(w,abs(F))/max(abs(F)));
subplot(2,1,2);
plot(w,abs(B))/max(abs(B)));

%idem upsample y resample
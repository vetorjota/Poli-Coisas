function y = pfsim(k,a,b,n,N)

a=pfprec(a,n); b=pfprec(b,n); k4=pfprec(4*k,n);

y=zeros(N,1);

y(1) = pfprec(k,n);
y(2) = pfprecsum( pfprec(3*k,n),pfprec(-a*k,n),n );

for i=3:N
    au = pfprec(a*y(i-1),n); bu = pfprec(b*y(i-2),n);
    y(i) = pfprecsum(k4, pfprecsum(-au,-bu,n) ,n);
end
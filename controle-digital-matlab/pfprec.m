function y=pfprec(x,n);
% trunca um numero com n casas decimais
y = fix(x*10^n)/(10^n);

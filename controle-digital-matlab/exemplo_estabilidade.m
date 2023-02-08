% Exemplo
% Estabilidade de um sistema

% O sistema
num = 1;
den = [1 0.9 0 3 3 -0.7];
T = 1;

% Polos
p = roots(den);
disp([p abs(p)])

% Resposta impulsiva
sistema = tf(num,den,T);
impulse(sistema);
axis([0 40 -50 50])

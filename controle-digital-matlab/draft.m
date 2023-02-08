T=0.2; xsi=0.3; wn=2.0
aa = exp(-T)+T-1;
bb = 1-exp(-T)*(T+1);
cc = exp(-T);

A = [aa 1; bb -1];
B = [1-2*exp(-T*wn*xsi)*cos(T*wn*sqrt(1-xsi^2)); ...
      exp(-2*T*wn*xsi)];

x = A\B;

Kc = x(1), beta = x(2),

ftmf = tf([Kc*A Kc*B],[1 (Kc*A+beta-1) (Kc*B-beta)],T)

ref  = tf([wn^2],[1 2*xsi*wn wn^2])

refd = c2d(ref,T,'match')
% exlgr

% Planta
Gpc = zpk([],[1,-2,-3],1);

% Discretização da planta
f = 10; T=1/f;
Gp = c2d(Gpc,T,'zoh');

% Projeto
sisotool('exlgr')
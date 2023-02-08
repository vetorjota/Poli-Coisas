%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Um exemplo de algoritmo de controle %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                  z
% Seja G(z) = ----------
%               z - 0.7
%      
%
% y(k) = 0.7*y(k-1) + u(k)
%

% Inicialização
clear all
n    = 10;
u    = ones(1,n);  % u é um degrau unitario
y    = zeros(1,n);
tu   = zeros(1,n);
talg = zeros(1,n);
ty   = zeros(1,n);

T = 0.001;
t = (0:n-1)*T;

% Loop
tic; while (toc<T) end
for k = 2:n
    tocanterior = toc;
    
    % u(k) = readAD;
    tu(k) = toc;
    
    y(k) = 0.7*y(k-1)+u(k);
    %fprintf('k:%d  --> y(k)=%g  u(k)=%g\n',k,y(k),u(k));
    x = inv(rand(10,10));
    talg(k) = toc;
    
    % writeD2A(y(k);
    ty(k) = toc;
    
    % waitbusy
    while ((toc - tocanterior)<T) end
    end

% Mostra os resultados
figure(1); 
clf;
stem(tu,u,'fill','k');
hold on
stem(ty,y,'fill','r');
axis([0 max([t ty]) 0 inf])
set(gca,'xtick',t)
hold off

figure(2);
clf;
dtu = tu-t;
dta = talg-tu;
dty = ty-talg;
for i=1:length(t)
    hold on;
    patch([0 dtu(i) dtu(i) 0 0], t(i) + T*[-0.2 -0.2 0.2 0.2 -0.2],'k');
    patch([dtu(i) dtu(i)+dta(i) dtu(i)+dta(i) dtu(i) dtu(i)], t(i) + T*[-0.2 -0.2 0.2 0.2 -0.2],'g');
    patch([dtu(i)+dta(i) dtu(i)+dta(i)+dty(i) dtu(i)+dta(i)+dty(i) dtu(i)+dta(i) dtu(i)+dta(i)], ...
           t(i) + T*[-0.2 -0.2 0.2 0.2 -0.2],'r');
    plot([dtu(i)+dta(i)+dty(i) T],[t(i) t(i)],'color',0.7*[1 1 1]);
    hold off
end

   



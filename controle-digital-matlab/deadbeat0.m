% Exemplo deadbeat0.m

% Parâmetros
f = 1;
td = [0:10];

% Planta (sem atraso)
Gps = zpk([],[-1],1);
% Atraso
theta = 2;

Gpz = tf(0.6321,[1 -0.3679 0 0],1/f);

% Controle (cf. notas de aula)
Gcz = tf(1.5820*[1 -0.3679 0 0],[1 0 0 -1],1/f);

% Simulando a resposta ao degrau
opt = simset('SrcWorkspace','current');
sim('deadbeat0sim',[],opt);

figure(1);
[ax,h1,h2]=plotyy(t,u2c.signals.values,...
                  t,y2c.signals.values);
set(get(ax(1),'Ylabel'),'String','Saída do controlador')              
set(get(ax(2),'Ylabel'),'String','Saída da planta') 

set(h1,'LineStyle',':','LineWidth',2)
set(h2,'LineWidth',3)

hold(ax(2),'on');
h3=plot(ax(2),td,y2d.signals.values,'ro');
hold(ax(2),'off');
              
xlabel('tempo (s)'); title('Considerando a planta Gc(z) discreta');
zoom on

figure(2);
[ax,h1,h2]=plotyy(t,u2c.signals.values,...
                  t,[y2c.signals.values y1c.signals.values]);
set(get(ax(1),'Ylabel'),'String','Saída do controlador')              
set(get(ax(2),'Ylabel'),'String','Saída da planta') 

set(h1,'LineStyle',':','LineWidth',2)
set(h2,'LineWidth',3)

hold(ax(2),'on');
h3=plot(ax(2),td,y2d.signals.values,'ro');
hold(ax(2),'off');
              
xlabel('tempo (s)'); title('Considerando a planta Gc(s) contínua');
zoom on

figure(1);
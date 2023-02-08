% Exemplo deadbeat1.m

% Parâmetros
f = 1;
td = [0:20];

% Planta
Gps = zpk([],[0 -0.1],0.1);

Gpz = c2d(Gps,1/f,'zoh');

% Controle (cf. FPW-pag.268)
Gcz = zpk([0.9048 0.07932],[-0.9672 0.4180],13.07,1/f);

% Simulando a resposta ao degrau
opt = simset('SrcWorkspace','current');
sim('deadbeat1sim',[],opt);

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
function varargout = ex_av_v(varargin)
% EX_AV_V M-file for ex_av_v.fig
%      EX_AV_V, by itself, creates a new EX_AV_V or raises the existing
%      singleton*.
%
%      H = EX_AV_V returns the handle to a new EX_AV_V or the handle to
%      the existing singleton*.
%
%      EX_AV_V('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in EX_AV_V.M with the given input arguments.
%
%      EX_AV_V('Property','Value',...) creates a new EX_AV_V or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before ex_av_v_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to ex_av_v_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help ex_av_v

% Last Modified by GUIDE v2.5 27-Oct-2008 17:51:49

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @ex_av_v_OpeningFcn, ...
                   'gui_OutputFcn',  @ex_av_v_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before ex_av_v is made visible.
function ex_av_v_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to ex_av_v (see VARARGIN)

% Função de transferência
G  = zpk([],[0 -1 -2],10);

handles.G = G;

% Choose default command line output for ex_av_v
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes ex_av_v wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = ex_av_v_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double

handles.f = str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.f = str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);



function edit5_Callback(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double

handles.Tav = 1/str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function edit5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.Tav = 1/str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);



function edit6_Callback(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit6 as text
%        str2double(get(hObject,'String')) returns contents of edit6 as a double

alfa = str2double(get(hObject,'String'));
if alfa>1
    alfa = 0.99;
    set(hObject,'String','0.99');
elseif alfa<=0
    alfa = 0.01;
    set(hObject,'String','0.01');
end
  
handles.alfa = alfa;

% Update handles structure
guidata(hObject, handles);


% --- Executes during object creation, after setting all properties.
function edit6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.alfa = str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

f = handles.f; T = 1/f; G = handles.G;
Tav = handles.Tav; alfa = handles.alfa;
graf = handles.graf;

% Discretizando
Gd = c2d(G,T,'zoh');

% Plano w
Gv = d2c(Gd,'tustin');

% Compensador (no plano w)
Av = tf([Tav 1],[alfa*Tav 1]);

% FTMA
Gma = series(Av,Gv);

% Bode
v = logspace(-2,3,400);
[m,p]=bode(Gv,v); m=squeeze(m); mdb=20*log10(m); p=squeeze(p);
[mma,pma]=bode(Gma,v); mma=squeeze(mma); mmadb=20*log10(mma); pma=squeeze(pma);
% Margens de ganho e fase
[mg,mp,vg,vp] = margin(Gma);
% Corrige a fase
while max(p)>0
    p = p-360;
end
while max(pma)>0
    pma = pma-360;
end

% Nyquist
vN = [logspace(-2,3,500) logspace(3,20,500)];
[reG,imG] = nyquist(Gv,vN); reG=squeeze(reG); imG=squeeze(imG);
[reGma,imGma] = nyquist(Gma,vN); reGma=squeeze(reGma); imGma=squeeze(imGma);
% Bola de estabilidade
rest = min(abs(reGma+j*imGma+1));
cest = rest*exp(j*[0:0.01:2*pi])-1;

if graf==1 | graf==2
    if graf==1
        subplot(2,1,1,'Parent',handles.uipanel8)
    else
        subplot(1,1,1,'Parent',handles.uipanel8)
    end
    set(gca,'fontsize',8);
    semilogx(v,mmadb,'linewidth',1.5,'color',[0.8 1 0.8]); hold on
    semilogx(v,mdb,'linewidth',1.5,'color',[0.2 0.6 0]);
    h=semilogx(vg*[1 1],[0 -20*log10(mg)],'linewidth',1.5,'color',[0 0 0]);
    if (20*log10(mg))<0
        set(h,'color',[1 0 0]);
    end;
    axis([1e-2 1e3 -100 50]);
    ylabel('Mod. de G(\omega),G(v) [dB]');
    set(gca,'ytick',[-150 -100 -50 0 50 100]);
    stitle = sprintf('< margem de ganho: %4.1f dB>    <margem de fase: %4.1f graus>',20*log10(mg),mp);
    title(stitle)
    if graf==2
        xlabel('freqüência fictícia v [rad/s')
    end
    grid on; hold off; zoom on;
end

if graf==1 | graf==3
    if graf==1
        subplot(2,1,2,'Parent',handles.uipanel8)
    else
        subplot(1,1,1,'Parent',handles.uipanel8)
    end
    set(gca,'fontsize',8);
    semilogx(v,pma,'linewidth',1.5,'color',[0.8 1 0.8]); hold on
    semilogx(v,p,'linewidth',1.5,'color',[0.2 0.6 0]);
    h=semilogx(vp*[1 1],[-180 mp-180],'linewidth',1.5,'color',[0 0 0]);
    if mp<0
        set(h,'color',[1 0 0]);
    end 
    axis([1e-2 1e3 -365 -85]);
    ylabel('Fase de G(\omega),G(v) [graus]');
    xlabel('freqüência fictícia v [rad/s]');
    set(gca,'ytick',[-360 -270 -180 -90]);
    grid on; hold off; zoom on;
end

if graf==4
    subplot(1,1,1,'Parent',handles.uipanel8)
    set(gca,'fontsize',8);
    plot(reGma+j*imGma,'linewidth',1.5,'color',[0.8 1 0.8]); hold on
    plot(reG+j*imG,'linewidth',1.5,'color',[0.2 0.6 0]);
    plot(cest,'r');
    plot([-5 1],[0 0],'k:');
    plot([0 0],[-2 2],'k:');
    plot(-1,0,'r+');
    axis equal;
    legend('c/ compensador','s/ compensador','location','NorthWest')
    axis([-5 1 -2 2]);
    hold off; zoom on
end

clc;
disp('------------------------------')
disp('Compensador discreto')
disp(' ')
Gav=c2d(Av,T,'tustin')
disp('------------------------------')


% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function pushbutton3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% --- Executes on selection change in popupmenu3.
function popupmenu3_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns popupmenu3 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu3

handles.graf = get(hObject,'Value');
% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function popupmenu3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.

handles.graf = get(hObject,'Value');
% Update handles structure
guidata(hObject, handles);

if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



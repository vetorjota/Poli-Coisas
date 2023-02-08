function varargout = approxctrl2(varargin)
% APPROXCTRL2 M-file for approxctrl2.fig
%      APPROXCTRL2, by itself, creates a new APPROXCTRL2 or raises the existing
%      singleton*.
%
%      H = APPROXCTRL2 returns the handle to a new APPROXCTRL2 or the handle to
%      the existing singleton*.
%
%      APPROXCTRL2('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in APPROXCTRL2.M with the given input arguments.
%
%      APPROXCTRL2('Property','Value',...) creates a new APPROXCTRL2 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before approxctrl2_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to approxctrl2_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help approxctrl2

% Last Modified by GUIDE v2.5 03-Oct-2008 11:16:52

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @approxctrl2_OpeningFcn, ...
                   'gui_OutputFcn',  @approxctrl2_OutputFcn, ...
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


% --- Executes just before approxctrl2 is made visible.
function approxctrl2_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to approxctrl2 (see VARARGIN)

% Inicialmente plotamos a curva contínua ideal
xsi=0.3; wn=2; f=5.0;

t = linspace(0,10,1000);
y = step(tf(wn^2,[1 2*xsi*wn wn^2]),t);


plot(t,y,'k')
axis([0 10 0 1.6])

xlabel('tempo (s)'); ylabel('Resposta ao degrau');

handles.xsi = xsi; handles.wn = wn; handles.f = f;

% Choose default command line output for approxctrl2
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes approxctrl2 wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = approxctrl2_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes during object creation, after setting all properties.
function axes1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: place code in OpeningFcn to populate axes1


% --- Executes on mouse press over axes background.
function axes1_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to axes1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



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

handles.fmin = str2double(get(hObject,'String'));
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

handles.fmin = str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);



function edit6_Callback(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit6 as text
%        str2double(get(hObject,'String')) returns contents of edit6 as a double

handles.fmax = str2double(get(hObject,'String'));
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

handles.fmax = str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

xsi = handles.xsi; wn = handles.wn; f = handles.f;
graf = handles.graf;

% controle contínuo base
Kc = wn^2;
b  = 2*xsi*wn;
ctrlbase = zpk(-1,-b,Kc);
% controle discreto base
ctrldbase = c2d(ctrlbase,1/f,'matched');

% controle contínuo Padé
A = [ 1 -1 0 ; 4*f -2*xsi*wn -1 ; 0 -wn^2 4*f ];
B = [ 2*xsi*wn-4*f ; wn^2 ; 0 ];
v = A\B;
KcPade = v(3);
bPade  = v(1);
ctrlPade = zpk(-1,-bPade,KcPade);
% controle discreto Padé
ctrldPade = c2d(ctrlPade,1/f,'matched');

% controle contínuo filtro 1a. ordem
A = [ 1 -1 0 ; 2*f -2*xsi*wn 0 ; 0 -wn^2 2*f ];
B = [2*xsi*wn-2*f ; wn^2 ; 0 ];
v = A\B;
KcFilt = v(3);
bFilt  = v(1);
ctrlFilt = zpk(-1,-bFilt,KcFilt);
% controle discreto filtro 1a. ordem
ctrldFilt = c2d(ctrlFilt,1/f,'matched');

% controle discreto Z
T = 1/f;
aa = exp(-T)+T-1;
bb = 1-exp(-T)*(T+1);
cc = exp(-T);

A = [aa 1; bb -1];
B = [1-2*exp(-T*wn*xsi)*cos(T*wn*sqrt(1-xsi^2)); ...
      exp(-2*T*wn*xsi)];

v = A\B;
KcZ = v(1);
bZ  = v(2);

ctrldZ = zpk(cc,-bZ,KcZ,T);

% Simula todo mundo
opt = simset('SrcWorkspace','current');
sim('approxctrlsim2',[],opt);
if graf==1
    plot(td,ybase.signals.values,'k',...
         td,ydbase.signals.values,'b',...
         td,ydPade.signals.values,'g',...
         td,ydFilt.signals.values,'m',...
         td,ydZ.signals.values,'c');
    axis([0 10 0 1.6]);
    legend('referência','discr.','discr.Pade','discr.Filt','discr. Z','Location','SouthEast');
    xlabel('tempo (s)'); ylabel('Resposta ao degrau - saída da planta');
    zoom on
elseif graf==2
    plot(td,ubase.signals.values,'k',...
         td,udbase.signals.values,'b',...
         td,udPade.signals.values,'g',...
         td,udFilt.signals.values,'m',...
         td,udZ.signals.values,'c');
    axis([0 10 -2.5 5]);
    legend('referência','discr.','discr.Pade','discr.Filt','discr. Z','Location','NorthEast');
    xlabel('tempo (s)'); ylabel('Resposta ao degrau - saída do controlador');
    zoom on
end

% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

xsi = handles.xsi; wn = handles.wn;
fmin = handles.fmin; fmax = handles.fmax;
graf = handles.graf;

fvec = fmin:0.5:fmax;

for i=1:length(fvec)
    f = fvec(i);
    
    % controle contínuo base
    Kc = wn^2;
    b  = 2*xsi*wn;
    ctrlbase = zpk(-1,-b,Kc);
    % controle discreto base
    ctrldbase = c2d(ctrlbase,1/f,'matched');

    % controle contínuo Padé
    A = [ 1 -1 0 ; 4*f -2*xsi*wn -1 ; 0 -wn^2 4*f ];
    B = [ 2*xsi*wn-4*f ; wn^2 ; 0 ];
    v = A\B;
    KcPade = v(3);
    bPade  = v(1);
    ctrlPade = zpk(-1,-bPade,KcPade);
    % controle discreto Padé
    ctrldPade = c2d(ctrlPade,1/f,'matched');

    % controle contínuo filtro 1a. ordem
    A = [ 1 -1 0 ; 2*f -2*xsi*wn 0 ; 0 -wn^2 2*f ];
    B = [2*xsi*wn-2*f ; wn^2 ; 0 ];
    v = A\B;
    KcFilt = v(3);
    bFilt  = v(1);
    ctrlFilt = zpk(-1,-bFilt,KcFilt);
    % controle discreto filtro 1a. ordem
    ctrldFilt = c2d(ctrlFilt,1/f,'matched');

    % controle discreto Z
    T = 1/f;
    aa = exp(-T)+T-1;
    bb = 1-exp(-T)*(T+1);
    cc = exp(-T);

    A = [aa 1; bb -1];
    B = [1-2*exp(-T*wn*xsi)*cos(T*wn*sqrt(1-xsi^2)); ...
         exp(-2*T*wn*xsi)];

    v = A\B;
    KcZ = v(1);
    bZ  = v(2);

    ctrldZ = zpk(cc,-bZ,KcZ,T);
    
    % Simula todo mundo
    opt = simset('SrcWorkspace','current');
    sim('approxctrlsim2',[],opt);
    if graf==1
        plot(td,ybase.signals.values,'k',...
             td,ydbase.signals.values,'b',...
             td,ydPade.signals.values,'g',...
             td,ydFilt.signals.values,'m',...
             td,ydZ.signals.values,'c');
        axis([0 10 0 1.6]);
        legend('referência','discr.','discr.Pade','discr.Filt','discr. Z','Location','SouthEast');
        xlabel('tempo (s)'); ylabel('Resposta ao degrau - saída da planta');
        zoom on
    elseif graf==2
        plot(td,ubase.signals.values,'k',...
             td,udbase.signals.values,'b',...
             td,udPade.signals.values,'g',...
             td,udFilt.signals.values,'m',...
             td,udZ.signals.values,'c');
        axis([0 10 -2.5 5]);
        legend('referência','discr.','discr.Pade','discr.Filt','discr. Z','Location','NorthEast');
        xlabel('tempo (s)'); ylabel('Resposta ao degrau - saída do controlador');
        zoom on
    end
    strtitle = sprintf('Varrendo ... %-8.2f Hz',f);
    title(strtitle);
    drawnow
end

% Update handles structure
guidata(hObject, handles);



% --- Executes during object creation, after setting all properties.
function pushbutton3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called



function edit7_Callback(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit7 as text
%        str2double(get(hObject,'String')) returns contents of edit7 as a double

handles.xsi = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function edit7_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.xsi = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);



function edit8_Callback(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit8 as text
%        str2double(get(hObject,'String')) returns contents of edit8 as a double

handles.wn = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function edit8_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.wn = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);


% --- Executes on selection change in popupmenu2.
function popupmenu2_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns popupmenu2 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu2

handles.graf = get(hObject,'Value');
% Update handles structure
guidata(hObject, handles);


% --- Executes during object creation, after setting all properties.
function popupmenu2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.graf = get(hObject,'Value');
% Update handles structure
guidata(hObject, handles);



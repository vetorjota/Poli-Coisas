function varargout = boded(varargin)
% BODED M-file for boded.fig
%      BODED, by itself, creates a new BODED or raises the existing
%      singleton*.
%
%      H = BODED returns the handle to a new BODED or the handle to
%      the existing singleton*.
%
%      BODED('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in BODED.M with the given input arguments.
%
%      BODED('Property','Value',...) creates a new BODED or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before boded_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to boded_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help boded

% Last Modified by GUIDE v2.5 18-Oct-2008 21:40:09

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @boded_OpeningFcn, ...
                   'gui_OutputFcn',  @boded_OutputFcn, ...
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


% --- Executes just before boded is made visible.
function boded_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to boded (see VARARGIN)

% Função de transferência
G  = tf(1,[1 1 0]);

handles.G = G;

% Choose default command line output for boded
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes boded wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = boded_OutputFcn(hObject, eventdata, handles) 
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

f = handles.f; T = 1/f; G = handles.G;
graf = handles.graf;

% Escolhendo w
wmin = 1e-2; wmax = max(1e2,pi/T);
w  = logspace(log10(wmin),log10(wmax),400);
wd = logspace(log10(wmin),log10(pi/T),400);
% Escala dos gráficos
mmin = -150; mmax = 50;
pmin = -275; pmax = -85;

% Discretizando
Gd = c2d(G,T,'zoh');

% Bode
[m,p]=bode(G,w); m=squeeze(m); mdb=20*log10(m); p=squeeze(p);
[md,pd]=bode(Gd,wd); md=squeeze(md); mddb=20*log10(md); pd=squeeze(pd);

if graf==1 | graf==2
    if graf==1
        subplot(2,1,1,'Parent',handles.uipanel8)
    else
        subplot(1,1,1,'Parent',handles.uipanel8)
    end
    set(gca,'fontsize',8);
    semilogx(w,mdb,'linewidth',1.5,'color',[1 0 0]); hold on
    semilogx(wd,mddb,'linewidth',1.5,'color',[0 0 1]);
    semilogx(pi/T*[1 1],[mmin,mmax],'k');
    axis([wmin wmax mmin mmax]);
    ylabel('Módulo de G(s),G(z) [dB]');
    set(gca,'ytick',[-150 -100 -50 0 50]);
    hold off;
    zoom on;
end

if graf==1 | graf==3
    if graf==1
        subplot(2,1,2,'Parent',handles.uipanel8)
    else
        subplot(1,1,1,'Parent',handles.uipanel8)
    end
    set(gca,'fontsize',8);
    semilogx(w,p,'linewidth',1.5,'color',[1 0 0]); hold on
    semilogx(wd,pd,'linewidth',1.5,'color',[0 0 1]);
    semilogx(pi/T*[1 1],[pmin,pmax],'k');
    axis([wmin wmax pmin pmax]);
    ylabel('Fase de G(s),G(z) [graus]');
    set(gca,'ytick',[-270 -180 -90]);
    hold off;
    zoom on;
end

% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


fmin = handles.fmin; fmax = handles.fmax;
graf = handles.graf; G= handles.G;

fvec = fmin:0.5:fmax;

for i=1:length(fvec)
    f = fvec(i); T = 1/f;

    % Escolhendo w
    wmin = 1e-2; wmax = max(1e2,pi/T);
    w  = logspace(log10(wmin),log10(wmax),400);
    wd = logspace(log10(wmin),log10(pi/T),400);
    % Escala dos gráficos
    mmin = -150; mmax = 50;
    pmin = -275; pmax = -85;
    
    % Discretizando
    Gd = c2d(G,T,'zoh');
    
    % Bode
    [m,p]=bode(G,w); m=squeeze(m); mdb=20*log10(m); p=squeeze(p);
    [md,pd]=bode(Gd,wd); md=squeeze(md); mddb=20*log10(md); pd=squeeze(pd);
    
    if graf==1 | graf==2
        if graf==1
            subplot(2,1,1,'Parent',handles.uipanel8)
        else
            subplot(1,1,1,'Parent',handles.uipanel8)
        end
        set(gca,'fontsize',8);
        semilogx(w,mdb,'linewidth',1.5,'color',[1 0 0]); hold on
        semilogx(wd,mddb,'linewidth',1.5,'color',[0 0 1]);
        semilogx(pi/T*[1 1],[mmin,mmax],'k');
        axis([wmin wmax mmin mmax]);
        ylabel('Módulo de G(s),G(z) [dB]');
        set(gca,'ytick',[-150 -100 -50 0 50]);
        hold off;
        strtitle = sprintf('Varrendo ... %-8.2f Hz',f);
        title(strtitle);

        zoom on;
    end

    if graf==1 | graf==3
        if graf==1
            subplot(2,1,2,'Parent',handles.uipanel8)
        else
            subplot(1,1,1,'Parent',handles.uipanel8)
        end
        set(gca,'fontsize',8);
        semilogx(w,p,'linewidth',1.5,'color',[1 0 0]); hold on
        semilogx(wd,pd,'linewidth',1.5,'color',[0 0 1]);
        semilogx(pi/T*[1 1],[pmin,pmax],'k');
        axis([wmin wmax pmin pmax]);
        ylabel('Fase de G(s),G(z) [graus]');
        set(gca,'ytick',[-270 -180 -90]);
        hold off;
        if graf==3
            strtitle = sprintf('Varrendo ... %-8.2f Hz',f);
            title(strtitle);
        end
        zoom on;
    end
    drawnow;
end

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



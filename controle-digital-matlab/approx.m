function varargout = approx(varargin)
% APPROX M-file for approx.fig
%      APPROX, by itself, creates a new APPROX or raises the existing
%      singleton*.
%
%      H = APPROX returns the handle to a new APPROX or the handle to
%      the existing singleton*.
%
%      APPROX('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in APPROX.M with the given input arguments.
%
%      APPROX('Property','Value',...) creates a new APPROX or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before approx_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to approx_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help approx

% Last Modified by GUIDE v2.5 05-Sep-2008 10:45:00

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @approx_OpeningFcn, ...
                   'gui_OutputFcn',  @approx_OutputFcn, ...
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


% --- Executes just before approx is made visible.
function approx_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to approx (see VARARGIN)

% Inicialmente calculamos a resposta do sistema contínuo.
xsi=0.3; wn=2;
siscont = tf([wn^2],[1 2*xsi*wn wn^2]);
step(siscont)
axis([0 10 0 1.5]);
set(gca,'box','on');

handles.xsi = xsi; handles.wn = wn;

% Choose default command line output for approx
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes approx wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = approx_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

handles.qv = str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);


% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

handles.qv = str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% quantizacao no tempo
qt = handles.qt;
if qt > 1000, qt = 1000; end
tq = linspace(0,1,qt);
sqt = sin(2*pi*tq);

% quantizacao no valor
qv = handles.qv;
h = 2/(qv-1);

sqvt = round((sqt+1)/h)*h - 1;

plot(handles.tc,handles.sc);
hold on;
stairs(tq,sqvt,'r');
h=plot(tq,sqvt,'mo');
set(h,'linewidth',3);
hold off;
axis([0 1 -1.1 1.1])


function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

handles.qt = str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);


% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

handles.qt = str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object deletion, before destroying properties.
function edit1_DeleteFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- If Enable == 'on', executes on mouse press in 5 pixel border.
% --- Otherwise, executes on mouse press in 5 pixel border or over edit1.
function edit1_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on key press with focus on edit1 and none of its controls.
function edit1_KeyPressFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  structure with the following fields (see UICONTROL)
%	Key: name of the key that was pressed, in lower case
%	Character: character interpretation of the key(s) that was pressed
%	Modifier: name(s) of the modifier key(s) (i.e., control, shift) pressed
% handles    structure with handles and user data (see GUIDATA)


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



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double

handles.fsen = str2double(get(hObject,'String'));
% Update handles structure
guidata(hObject, handles);


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.fsen = str2double(get(hObject,'String'));
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

f = handles.f;
xsi = handles.xsi; wn = handles.wn;
graf = handles.graf;

siscont   = tf([wn^2],[1 2*xsi*wn wn^2]);
% tustin
sistustin = c2d(siscont,1/f,'tustin');
% casamento polo-zero 1
z = [-1; -1];
p = [exp( -wn*(xsi-sqrt(xsi^2-1))/f ) ; exp( -wn*(xsi+sqrt(xsi^2-1))/f )];
k = 1*(1-p(1))*(1-p(2))/4;
sismatch1 = zpk(z,p,k,1/f);
% casamento polo-zero 2
z2 = [-1];
k2 = 1*(1-p(1))*(1-p(2))/2;
sismatch2 = zpk(z2,p,k2,1/f);

if graf==1
    step(siscont,'k-',sistustin,'g-',sismatch1,'r-',sismatch2,'m-')
    axis([0 10 0 1.5]);
    set(gca,'box','on');
    legend('Contínuo','Tustin','Cas. PZ (próprio)','Cas. PZ (estr. próprio)','Location','SouthEast')
elseif graf==2
    bode(siscont,'k-',sistustin,'g-',sismatch1,'r-',sismatch2,'m-')
    h=get(gcf,'children')
    for i=1:length(h)
        strtype = get(h(i),'type');
        if strncmp(strtype,'axes',2)
            if strncmp(get(get(h(i),'ylabel'),'string'),'Phase (deg)',2)
                set(h(i),'ylim',[-270 0]);
            elseif strncmp(get(get(h(i),'ylabel'),'string'),'Magnitude (dB)',2)
                set(h(i),'ylim',[-80 10]);
            end
        end
    end
        
    set(gca,'box','on');
    legend('Contínuo','Tustin','Cas. PZ (próprio)','Cas. PZ (estr. próprio)','Location','SouthWest')
end
  

zoom on

% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

xsi = handles.xsi; wn = handles.wn;
fmin = handles.fmin; fmax = handles.fmax;
graf = handles.graf;

fvec = fmin:0.1:fmax;

for i=1:length(fvec)
    f = fvec(i);

    siscont   = tf([wn^2],[1 2*xsi*wn wn^2]);
    % tustin
    sistustin = c2d(siscont,1/f,'tustin');
    % casamento polo-zero 1
    z = [-1; -1];
    p = [exp( -wn*(xsi-sqrt(xsi^2-1))/f ) ; exp( -wn*(xsi+sqrt(xsi^2-1))/f )];
    k = 1*(1-p(1))*(1-p(2))/4;
    sismatch1 = zpk(z,p,k,1/f);
    % casamento polo-zero 2
    z2 = [-1];
    k2 = 1*(1-p(1))*(1-p(2))/2;
    sismatch2 = zpk(z2,p,k2,1/f);

    if graf==1
        step(siscont,'k-',sistustin,'g-',sismatch1,'r-',sismatch2,'m-')
        axis([0 10 0 1.5]);
        set(gca,'box','on');
        legend('Contínuo','Tustin','Cas. PZ (próprio)','Cas. PZ (estr. próprio)','Location','SouthEast')
    elseif graf==2
        bode(siscont,'k-',sistustin,'g-',sismatch1,'r-',sismatch2,'m-')
        h=get(gcf,'children')
        for i=1:length(h)
            strtype = get(h(i),'type');
            if strncmp(strtype,'axes',2)
                if strncmp(get(get(h(i),'ylabel'),'string'),'Phase (deg)',2)
                    set(h(i),'ylim',[-270 0]);
                elseif strncmp(get(get(h(i),'ylabel'),'string'),'Magnitude (dB)',2)
                    set(h(i),'ylim',[-80 10]);
                end
            end
        end
        
        set(gca,'box','on');
        legend('Contínuo','Tustin','Cas. PZ (próprio)','Cas. PZ (estr. próprio)','Location','SouthWest')
    end

    strtitle = sprintf('Varrendo ... %-8.2f Hz',f);
    title(strtitle);
    drawnow
end
zoom on


% --- Executes during object creation, after setting all properties.
function pushbutton3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called


% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1

handles.graf = get(hObject,'Value');
% Update handles structure
guidata(hObject, handles);


% --- Executes during object creation, after setting all properties.
function popupmenu1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
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



function varargout = rlanalysisHP(varargin)
% RLANALYSISHP M-file for rlanalysisHP.fig
%      RLANALYSISHP, by itself, creates a new RLANALYSISHP or raises the existing
%      singleton*.
%
%      H = RLANALYSISHP returns the handle to a new RLANALYSISHP or the handle to
%      the existing singleton*.
%
%      RLANALYSISHP('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in RLANALYSISHP.M with the given input arguments.
%
%      RLANALYSISHP('Property','Value',...) creates a new RLANALYSISHP or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before rlanalysisHP_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to rlanalysisHP_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help rlanalysisHP

% Last Modified by GUIDE v2.5 21-Oct-2008 17:56:07

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @rlanalysisHP_OpeningFcn, ...
                   'gui_OutputFcn',  @rlanalysisHP_OutputFcn, ...
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


% --- Executes just before rlanalysisHP is made visible.
function rlanalysisHP_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to rlanalysisHP (see VARARGIN)

% Planta
Gpc = tf(1,[1 1 0]); handles.Gpc = Gpc;

% Eixo 1
axes(handles.axes1)
set(gca,'fontsize',8)
zgrid;
axis equal;
axis([-1 1 0 1.2])

% Eixo 2
axes(handles.axes2)
set(gca,'box','on','xtick',[],'ytick',[])

% Choose default command line output for rlanalysisHP
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes rlanalysisHP wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = rlanalysisHP_OutputFcn(hObject, eventdata, handles) 
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

axes(handles.axes1)
f = handles.f; hz = handles.hz;
xsih = handles.xsih; wnh = handles.wnh;
xsip = handles.xsi; wnp = handles.wn;

ppos = get(gca,'CurrentPoint'); xp = ppos(1,1); yp = ppos(1,2);
rp = sqrt(xp^2+yp^2); 
fp = atan(yp/xp);
if fp<0, fp = fp+pi; end;
if ( yp>0 ) & ( rp<1 )
    lnf2 = ( log(rp)/fp )^2;
    xsip = sqrt( lnf2/(1+lnf2) ); wnp  = -log(rp)*f/xsip;
    xsip = round(xsip*100)/100; wnp = round(wnp*100)/100;
    zo = exp( (wnp*(-xsip + sqrt(xsip^2-1)))/f );
    
    % Atualiza o plot
    hold on
    delete(hz)
    hz = plot( real(zo),imag(zo),'o',...
               'MarkerEdgeColor','k',...
               'MarkerFaceColor','g',...
               'MarkerSize',6 );
    handles.hz = hz;            
    axis([-1 1 0 1.2])
    hold off
    
    % Atualiza os campos
    set(xsih,'String',num2str(xsip,2));
    set(wnh,'String',num2str(wnp,2));
    
    % Atualiza o degrau
    axes(handles.axes2)
    set(gca,'fontsize',6)

    [ydeg,tdeg]=step( c2d(tf([wnp^2],[1 2*xsip*wnp wnp^2]),1/f,'match') );
    [tt,yy]=stairs(tdeg,ydeg);
    plot(tt,yy,'g',[0 10],[1 1],'k');
    axis([0 10 0 1.5])

end

handles.xsi = xsip; handles.wn = wnp;
% Update handles structure
guidata(hObject, handles);   
    





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


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

Gpc = handles.Gpc;
Kc = handles.Kc; a = handles.a; b = handles.b;
f = handles.f; T = 1/f;
flMp = handles.flMp; fltr = handles.fltr; flts = handles.flts;
Mpmin = handles.Mpmin; Mpmax = handles.Mpmax;
trmin = handles.trmin; trmax = handles.trmax;
tsmin = handles.tsmin; tsmax = handles.tsmax;

% Na figura maior (axes1)
axes(handles.axes1); cla
set(gca,'fontsize',8)
zgrid
hold on
axis equal;

% Mp
if flMp
    ln2 = (log(Mpmin/100))^2; if ln2>1e16, ln2=1e16; end   
    xsimin = sqrt( ln2/(ln2+pi^2) );
    ln2 = (log(Mpmax/100))^2;
    xsimax = sqrt( ln2/(ln2+pi^2) );
    
    wnvec = linspace(0,pi*f/sqrt(1-xsimin^2),200);
    zMpmin = exp( wnvec*(-xsimin+j*sqrt(1-xsimin^2))/f );
    wnvec = linspace(0,pi*f/sqrt(1-xsimax^2),200);
    zMpmax = exp( wnvec*(-xsimax+j*sqrt(1-xsimax^2))/f );
    hp=patch( real([zMpmin fliplr(zMpmax)]),imag([zMpmin fliplr(zMpmax)]),...
             [0 0 1],...
             'EdgeColor',[0 0 1],...
             'FaceAlpha',0.2,...
             'HitTest','off');
    plot(real(zMpmax),imag(zMpmax),'linewidth',2,'color',[0 0 1],'HitTest','off');
end

if fltr
    if trmin<0.5/f, trmin=0.5/f; end
    xsivec = linspace(0,1,200);
    xsivecloop = zeros(1,100);
    wnvecmin = ( pi - acos(xsivec) )./( trmin*sqrt(1-xsivec.^2) );
    wnvecmax = ( pi - acos(xsivec) )./( trmax*sqrt(1-xsivec.^2) );
    wnvecloop = linspace(pi/(2*trmax),pi/(2*trmin),100);
    wnveclim = pi*f./sqrt(1-xsivec.^2);
    wnvecmin = min([wnvecmin;wnveclim]);
    wnvecmax = min([wnvecmax;wnveclim]);
    ztrmin = exp( wnvecmin.*(-xsivec+j*sqrt(1-xsivec.^2))/f );
    ztrmax = exp( wnvecmax.*(-xsivec+j*sqrt(1-xsivec.^2))/f );
    ztrloop = exp( wnvecloop.*(-xsivecloop+j*sqrt(1-xsivecloop.^2))/f );
    hp=patch( real([ztrmin fliplr(ztrmax) ztrloop]),imag([ztrmin fliplr(ztrmax) ztrloop]),...
             [1 0 0],...
             'EdgeColor',[1 0 0],...
             'FaceAlpha',0.2,...
             'HitTest','off');
    plot(real(ztrmax),imag(ztrmax),'linewidth',2,'color',[1 0 0],'HitTest','off');
end

if flts
    fzts = linspace(0,pi,200);
    mztsmin = exp(-4/(tsmin*f));
    mztsmax = exp(-4/(tsmax*f));
    ztsmin = mztsmin*(cos(fzts)+j*sin(fzts));
    ztsmax = mztsmax*(cos(fzts)+j*sin(fzts));
    
    hp=patch( real([ztsmin fliplr(ztsmax)]),imag([ztsmin fliplr(ztsmax)]),...
             [0.871 0.49 0],...
             'EdgeColor',[0.871 0.49 0],...
             'FaceAlpha',0.2,...
             'HitTest','off');
    plot(real(ztsmax),imag(ztsmax),'linewidth',2,'color',[0.871 0.49 0],'HitTest','off');
end

% Planta
Gpd = c2d(Gpc,T,'zoh');
pp = [roots(cell2mat(Gpd.den))]
zp = [roots(cell2mat(Gpd.num))]
% Controle
Gcd = tf([1 -a],[1 -b],T);
pc = [b]; %já sei quais são...
zc = [a]
% FTMA
Gma = series(Gcd,Gpd);
% FTMF
Gmf = feedback(series(tf(Kc,1,T),Gma),1);
pmf = roots(cell2mat(Gmf.den))
% LGR
%kvec = [linspace(0,0.1,500),linspace(0.1,1,500),logspace(0,2,100) 1e12];
[r,kvec] = rlocus(Gma);
for i=1:size(r,1)
    plot(real(r(i,:)),imag(r(i,:)),'color',[0 150 50]/255,'linewidth',2)
end
% planta em violeta
plot(real(pp),imag(pp),'x','markersize',10,'linewidth',1.5,'color',[200 100 200]/255)
plot(real(zp),imag(zp),'o','markersize',10,'linewidth',1.5,'color',[200 100 200]/255)
% compensador em azul deserto
plot(real(pc),imag(pc),'x','markersize',10,'linewidth',1.5,'color',[50 100 150]/255)
plot(real(zc),imag(zc),'o','markersize',10,'linewidth',1.5,'color',[50 100 150]/255)
% polos de malha fechada em vermelho
plot(real(pmf),imag(pmf),'s','markersize',10,'linewidth',1.5,'color',[1 0 0])

axis([-1 1 0 1.2])
zoom on
hold off

% Na figura menor
axes(handles.axes2)
set(gca,'fontsize',6)

[ydeg,tdeg]=step(Gmf);
[tt,yy]=stairs(tdeg,ydeg);
plot(tt,yy,'g',[0 10],[1 1],'k');
axis([0 10 0 1.5])

%set(gca,'box','on','xtick',[],'ytick',[])

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

handles.Kc = str2double(get(hObject,'String'));
handles.Kch = hObject;

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

handles.Kc = str2double(get(hObject,'String'));
handles.Kch = hObject;

% Update handles structure
guidata(hObject, handles);



function edit8_Callback(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit8 as text
%        str2double(get(hObject,'String')) returns contents of edit8 as a double

handles.a = str2double(get(hObject,'String'));
handles.ah = hObject;

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

handles.a = str2double(get(hObject,'String'));
handles.ah = hObject;

% Update handles structure
guidata(hObject, handles);


% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton1

handles.flMp = get(hObject,'Value');

% Update handles structure
guidata(hObject, handles);



function edit9_Callback(hObject, eventdata, handles)
% hObject    handle to edit9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit9 as text
%        str2double(get(hObject,'String')) returns contents of edit9 as a double

handles.Mpmin = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function edit9_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.Mpmin = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);


function edit10_Callback(hObject, eventdata, handles)
% hObject    handle to edit10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit10 as text
%        str2double(get(hObject,'String')) returns contents of edit10 as a double

handles.Mpmax = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function edit10_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.Mpmax = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in radiobutton2.
function radiobutton2_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton2
handles.fltr = get(hObject,'Value');

% Update handles structure
guidata(hObject, handles);


function edit11_Callback(hObject, eventdata, handles)
% hObject    handle to edit11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit11 as text
%        str2double(get(hObject,'String')) returns contents of edit11 as a double

handles.trmin = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function edit11_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.trmin = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);


function edit12_Callback(hObject, eventdata, handles)
% hObject    handle to edit12 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit12 as text
%        str2double(get(hObject,'String')) returns contents of edit12 as a double

handles.trmax = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function edit12_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit12 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.trmax = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in radiobutton3.
function radiobutton3_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton3
handles.flts = get(hObject,'Value');

% Update handles structure
guidata(hObject, handles);


function edit13_Callback(hObject, eventdata, handles)
% hObject    handle to edit13 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit13 as text
%        str2double(get(hObject,'String')) returns contents of edit13 as a double

handles.tsmin = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function edit13_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit13 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.tsmin = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);


function edit14_Callback(hObject, eventdata, handles)
% hObject    handle to edit14 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit14 as text
%        str2double(get(hObject,'String')) returns contents of edit14 as a double

handles.tsmax = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);


% --- Executes during object creation, after setting all properties.
function edit14_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit14 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.tsmax = str2double(get(hObject,'String'));

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function radiobutton1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called
handles.flMp = get(hObject,'Value');

% Update handles structure
guidata(hObject, handles);


% --- Executes during object creation, after setting all properties.
function radiobutton2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called
handles.fltr = get(hObject,'Value');

% Update handles structure
guidata(hObject, handles);


% --- Executes during object creation, after setting all properties.
function radiobutton3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called
handles.flts = get(hObject,'Value');

% Update handles structure
guidata(hObject, handles);



function edit15_Callback(hObject, eventdata, handles)
% hObject    handle to edit15 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit15 as text
%        str2double(get(hObject,'String')) returns contents of edit15 as a double

handles.b = str2double(get(hObject,'String'));
handles.bh = hObject;

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function edit15_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit15 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

handles.b = str2double(get(hObject,'String'));
handles.bh = hObject;

% Update handles structure
guidata(hObject, handles);


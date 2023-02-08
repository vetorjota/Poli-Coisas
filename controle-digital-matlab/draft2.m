 Mpmin = 10; Mpmax = 30;
    ln2 = (log(Mpmin/100))^2;   
    xsimin = sqrt( ln2/(ln2+pi^2) );
    ln2 = (log(Mpmax/100))^2;
    xsimax = sqrt( ln2/(ln2+pi^2) );
    
    wnvec = linspace(0,pi*f/sqrt(1-xsimin^2),200);
    zMpmin = exp( wnvec*(-xsimin+j*sqrt(1-xsimin^2))/f );
    wnvec = linspace(0,pi*f/sqrt(1-xsimax^2),200);
    zMpmax = exp( wnvec*(-xsimax+j*sqrt(1-xsimax^2))/f );
    
    figure(2)
    plot(zMpmin)
    hold on
    plot(zMpmax)
    zgrid
    
    hp=patch( real([zMpmin fliplr(zMpmax)]),imag([zMpmin fliplr(zMpmax)]),[0 0 1] )
    set(hp,'EdgeColor',[0 0 1],'FaceAlpha',0.2)
    
 trmin=0.5; trmax=2
 
    xsivec = linspace(0,1,200);
    wnvecmin = ( pi - acos(xsivec) )./( trmin*sqrt(1-xsivec.^2) );
    wnvecmax = ( pi - acos(xsivec) )./( trmax*sqrt(1-xsivec.^2) );
    wnveclim = pi*f./sqrt(1-xsivec.^2);
    wnvecmin = min([wnvecmin;wnveclim]);
    wnvecmax = min([wnvecmax;wnveclim]);
    ztrmin = exp( wnvecmin.*(-xsivec+j*sqrt(1-xsivec.^2))/f );
    ztrmax = exp( wnvecmax.*(-xsivec+j*sqrt(1-xsivec.^2))/f );
    
    figure(3)
    plot(ztrmin)
    hold on
    plot(ztrmax)
    zgrid
    
    hp=patch( real([ztrmin fliplr(ztrmax)]),imag([ztrmin fliplr(ztrmax)]),[1 0 0] )
    set(hp,'EdgeColor',[1 0 0],'FaceAlpha',0.2)

tsmin=5; tsmax=10;
    xsivec = [linspace(0.005,0.095,198) linspace(0.1,1,200)];
    wnvecmin = 4./(tsmin*xsivec);
    wnvecmax = 4./(tsmax*xsivec);
    wnveclim = pi*f./sqrt(1-xsivec.^2);
    wnvecmin = min([wnvecmin;wnveclim]);
    wnvecmax = min([wnvecmax;wnveclim]);
    ztsmin = exp( wnvecmin.*(-xsivec+j*sqrt(1-xsivec.^2))/f );
    ztsmax = exp( wnvecmax.*(-xsivec+j*sqrt(1-xsivec.^2))/f );

    figure(4)
    plot(ztsmin)
    hold on
    plot(ztsmax)
    zgrid
    
    hp=patch( real([ztsmin fliplr(ztsmax)]),imag([ztsmin fliplr(ztsmax)]),[0.871 0.49 0] )
    set(hp,'EdgeColor',[0.871 0.49 0],'FaceAlpha',0.2)
    
wn=2; xsi=0.3;    
    hz = plot( exp( (wn.*(-xsi + sqrt(xsi^2-1)))/f ),'o',...
                'MarkerEdgeColor','k',...
                'MarkerFaceColor','g',...
                'MarkerSize',6 );
            
waitforbuttonpress
ppos = get(gca,'CurrentPoint'); xp = ppos(1,1); yp = ppos(1,2);
rp = sqrt(xp^2+yp^2); fp = atan(yp/xp);

lnf2 = ( log(rp)/fp )^2;
xsip = sqrt( lnf2/(1+lnf2) );
wnp  = -log(rp)*f/xsip;
xsip = round(xsip*100)/100; wnp = round(wnp*100/100);
[xsip wnp]

            
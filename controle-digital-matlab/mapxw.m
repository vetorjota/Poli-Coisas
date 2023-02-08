xvec = [0.0:0.1:1.0];
wvec = [0 2 4 6 8 10 12 14 16 18 20];

w = [0 logspace(-6,6,10000)];
x1 = 0.4; x2 = 0.8;

s1 = w.*(-x1 + sqrt(x1^2-1));
s2 = w.*(-x2 + sqrt(x2^2-1));

z1 = exp(s1);
z2 = exp(s2);



figure(1);
hold off
plot(s1,'b','linewidth',2)
hold on
plot(s2,'r','linewidth',2)
sgrid(xvec,wvec);
axis square; axis equal
axis([-19 1 -10 10])
xlabel('Real(s)'); ylabel('Imag(s)');
hold off

figure(2);
hold off
plot(z1,'b','linewidth',2)
hold on
plot(z2,'r','linewidth',2)
zgrid;
axis square; axis equal
xlabel('Real(z)'); ylabel('Imag(z)');
hold off
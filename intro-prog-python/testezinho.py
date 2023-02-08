def f(x):
    return x** 5 -1
def fp(x):
    return 5* x **4
    



def newton(f, fp, x, eps, maxiter):

    i=0    
    while i < maxiter:   #eps seria o "erro aceitável" da máquina

        if abs(fp(x)) < eps:
            return (-1,0)
        
        novo_x = x - f(x)/(fp(x))
        x = novo_x

        i+=1
        
        if abs(f(x)) < eps:
            return (i,x)


    if i == maxiter:
        return (-1,0)


def main():
    print(newton(f,fp,complex(-1,2),1e-8,100))

main()

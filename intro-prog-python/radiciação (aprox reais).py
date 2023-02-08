
''' calculando raiz quadrada aproximada de x atraves da sequencia'''

def raiz_quadrada(x,eps):

    r = x
    diferenca = eps 

    while diferenca >= eps:

        r_ant = r
        r = (r + x/r) /2
        diferenca = abs (r - r_ant)

    return r

def main():
    x = float(input('digite x : '))
    eps = float(input(' digite epsilon : '))

    print('o valor aproximado para raiz quadrada de %f é %f' %(x,raiz_quadrada(x,eps)))

main()
    

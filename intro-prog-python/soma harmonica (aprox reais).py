
'''calculando "soma harmônica de um número n'''


def harmonico(n):

    soma = 0
    for denominador in range (1,n+1):
        soma += 1/denominador

    return soma



def harmonico2(n):

    soma = 0
    for denominador in range (n,0,-1):
        soma += 1/denominador

    return soma


def main():

    n = int (input ("Digite o valor de n: "))
    print('O número harmônico de H%d somado da esquerda para direita é : %.20f .' %(n,harmonico(n)))
    print('O número harmônico de H%d somado da direita para esquerda é : %.20f .' %(n,harmonico2(n)))


    print()
    print("===extra===")
    print(' diferença entre esses números é ' ,abs( (harmonico(n) - harmonico2(n)) ))
    print( n / harmonico2(n))

main()


    
        

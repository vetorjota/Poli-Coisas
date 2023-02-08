'''função que calcula fatorial de um numero'''


def fatorial_recursiva(n):
    '''(int) -> int
    recebe n devolte fatorial desse numero'''

    if n == 0 or n == 1:    #caso base, caso trivial. conhecemos essa solução
        return 1
    else:                   #para qualquer n > 0 , n!  =  n* (n-1)!
        return n * fatorial_recursiva(n-1)


def fatorial(n):
    '''(int) -> int'''

    fat = 1
    i = 2
    while i <=n:
        fat *=i
        i += 1

    return fat


def main():

    numero = int(input("Digite um número para o qual se deseja calcular o fatorial:"))
    print("O fatorial de %d é : %d." %(numero, fatorial(numero)))
    print("O fatorial --calculado com recursão-- de %d é %d. "  %(numero, fatorial_recursiva(numero)))

main()





#NOTAS DE AULA | ASSUNTO : RECURSÃO
'''main
    numero= 3
        fatorial_recursiva
            n = 3
            devolve 3 * ___
                        |fatorial_recursiva
                            n = 3-1 = 2
                            devolve 2 * ___
                           ^             |fatorial_recursiva
                           |                n = 2-1 = 1
                           |                devolve 1 * ___  (supondo que eu não tivesse colocado o "or n == 1", se fosse só o n == 0
                           |                ^            |fatorial_recursiva
                           |                |              n = 1-1 =0
                           |                |               devolve 1
                           |                |                       |
                           |                -------------------------
                           |                |
                           |                |
                           |                --> devolve 1
                           |                             |
                           |                             |
                           ------------------------------

                    envolve pilha de execução'''



            

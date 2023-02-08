''' função de potência, que vai elevar um numero a outro '''
#primeiro vamos usar a solução tradicional, depois vamos pensar na solução recursiva.


def potencia(x,n):
    '''recebe base, expoente'''

    pot = 1    # se n for 0, devolve 1 pois qualquer número elevado a 0 é um.
    while n > 0:    #se n for 1, devolve 1 * x = x
        pot *= x     #<--|
        n -= 1

    '''opção: pot = x  e  while n > 1'''

    return pot

def main():
    base = float(input("Digite a base da potência: " ))
    expoente = int(input("Digite um expoente (natural) :"))

    resultado = potencia (base,expoente)
    resultado_rec = potencia_recursiva (base,expoente)
    
    print ("O numero %f elevado a %d é: %f ." %(base, expoente, resultado))
    print ("O numero %f elevado com recursão a %d é: %f ." %(base, expoente, resultado_rec))



def potencia_recursiva (x,n):

    #temos que definir um ponto de parada, o caso base, que deve ser conhecido, ou definido, sem a função ser chamada

    if n == 0:
        return 1
    else:
        return x * potencia_recursiva(x,n-1)

    '''opção: usar uma variavel resultado e depois retorná-la'''

main()




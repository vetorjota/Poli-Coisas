
'''agora vamos calcular, dado um numero real x e um numero real epsilon positivo e diferente de 0, calcular aproximação de e ^x
, 'e' sendo o número de euler, por meio da seguinte série infinita:

e^x = 1 + x^1/1! + x^2 / 2! + x^3 / 3! + ... + x^k / k! + ...

inclui na aprox todos os termos ate o primeiro de valor absoluto menor do que epsilon (incluindo)
'''

def exponencial (x,eps):

    soma = 1
    termo = 1

    expoente = 1
    fat = 1
    while termo >= eps or -termo >= eps:  #o mesmo que while abs(termo)>=eps
        termo = x**expoente / fat
        soma += termo
        expoente += 1
        fat *= expoente


    return soma

def exponencial2 (x,eps):
    a='nao sei o q fazer'

def main():
    x = float(input("Digite o valor de x: "))
    eps = float(input("Digite o valor de epsilon: "))

    print('O valor aproximado de e elevado a %f é %f .' %(x, exponencial(x,eps)))

main()

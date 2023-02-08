''' seq de fibonacci :  devolve k-ésimo número'''


def fibo(n):

    termo_novo = termo1 = termo2 = 1

    for i in range(3,n+1) :
        termo_novo = termo1 + termo2
        termo1 = termo2
        termo2 = termo_novo

    return termo_novo

def main():

    k = int(input("Digite a posiçao e interesse da sequência de fibonacci: "))
    print("o %dº número da sequência de Fibonacci é %d . Obrigada! " %(k,fibo(k)))
    print("o %dº número da sequencia de Fibonacci, recursivamente calculado, é %d. Bom dia! " %(k,fibo_rec(k)))




def fibo_rec(n):

    if n >= 3:
        return fibo_rec(n-1) + fibo_rec(n-2)
    else:
        return 1



main()

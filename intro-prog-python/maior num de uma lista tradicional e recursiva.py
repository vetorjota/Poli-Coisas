''' função q vai encontrar o maior valor de uma lista e inteiros q contem ao menos um numero.'''

def maior(L):
    m = L[0]

    for i in range (1,len(L)):     #1 pq já começa da primeira posição 0
        if L[i] > m:
            m = Li[i]

    return m


def main():
    n = int(input("Digite o tamanho da lista de números: "))
    lista=[]

    for i in range (1,n+1):
        lista.append(int(input("Digite o %d º número da sequência: " %i)))

    print("o maior valor da lista é:", maior(lista))
    print("o maior valor da lista, encontrado por recursão, é: " , maior2(lista))


def maior_rec(L,tamanho):
    '''L é a lista
     tamanho é tamanho da lista'''

    if tamanho == 1:   #caso base, em que a lista só tem um elemento
        return L [0]
    else:
        maior_el_resto_lista = maior_rec(L,tamanho-1)
        if L[tamanho-1] > maior_el_resto_lista:
            return L[tamanho-1]
        else:
            return maior_el_resto_lista


def maior2(L):      #"casquinha" de função, só para complementar o código (perfumaria) p/ q o usuário não se preocupe com o tamanho da lista, nesse caso
    return maior_rec(L,len(L))



main()

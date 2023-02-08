'''aprendendo algoritmos de ordenação
vamos ordenar uma lista dada em ordem crescente'''


def troca(L,i,j):
    aux = L[i]
    L[i] = L[j]
    L[j] = aux

def encontra_maior (L,fim):
    #fim é a ultima posiçao a ser olhada em L (que não pode ser vazia)
    pos_maior = 0

    for i in range (1,fim+1):
        if L[i] > L[pos_maior]:
            pos_maior = i

    return pos_maior


def ordenacao(lista):

    for i in range (len(lista) -1,0,-1):
        pos_maior = encontra_maior(lista,i)
        troca(lista,i,pos_maior)     #coloca na pos i o maior elemento da lista até i


def main():

    tam_lista = int(input('digite tamanho da lista: '))
    lista = []
    for i in range(len(tam_lista)):
        
        lista.append (input('mais um elemento:'))


    ordenacao(lista)
    print('a lista ordenada fica', lista)


main()

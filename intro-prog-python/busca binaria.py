
'''buscas recursivas'''


def busca_binaria_rec(lista,inicio,fim,x):

    #a fç devolve a pos de x na lista entre as pos inicio e fim
    #se v mao esta na sublista, devolve none

    if inicio > fim:
        return None

    meio = (inicio+fim) // 2

    if x == lista[meio]:
        return meio

    if x> lista [meio]:
        return busca_binaria_rec(lista,meio+1,fim,x)

    #se a execução chegou até aqui, x < lista[meio]
    return busca_binaria_rec(lista,inicio,meio-1,x)


#=======# teste #======#

L = [12,29,56,78,78,78,91,92,100]

testes = [29,78,25]

for valor in testes:
    pos = busca_binaria_rec (L,0,len(L)-1,valor)
    if pos is None:
        print(valor,"não esta na lista", L)
    else:
        print(valor,"está na posição %d da lista" %pos , L)

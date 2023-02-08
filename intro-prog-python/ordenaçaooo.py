''' algoritmos de ordenação '''


def main():
    print("Algoritmos de ordenação")

    print("Obs.: para eficácia do método, todos os elementos devem ser ou strings, ou números reais.")

    n = int(input("Insira o tamanho da lista: "))
    lista = []
    for i in range (n):
        lista.append(input("Digite o elemento número %d da lista a ser ordenada"%(i+1)))

    notimes = True
    while notimes:
        notimes = False
        res = input("Qual algoritmo de ordenação você deseja ulizar?\n=== 1 - Bolha === 2 - Inserção === 3 - Partições === \n=== 4 - Seleção === 5 - Divisão e Conquista === \n\t").lower()
        
        conv(lista)
        if res == 1 or res == 'bolha':
            bubble(lista)

        elif res == 2 or res == 'inserção':
            insertion(lista)

        elif res == 3 or res == 'partições':
            quicksort(lista)

        elif res == 4 or res == 'seleção':
            selection(lista)

        elif res == 5 or res == 'divisão e conquista':
            mergesort(lista)

        else:
            print("Tente digitar o código do algoritmo.")
            notimes = True
                        
    
        

def conv(lista_de_strings):
    if type (lista_de_strings[0]) is float:
        lista_conv = []
        for el in lista_de_strings:
            lista_conv.append(float(el))
    
        return lista_conv
    return lista_de_strings


def bubble(l):

    #compara dois a dois
    k = 0
    while k < (len(l)-1):
        if l[k] > l[k+1]:
            aux = l [k+1]
            l[k+1] = l[k]
            l[k] = aux
            k+=1

        elif l[k+1] <= l[k]:
            k+=1

    print ("A lista ordenada por Bolha fica:\n",l)

def insertion(l):

    return

def quicksort(l):

    return

def selection (l):

    return

def mergesort (l):

    return


main()
            









            

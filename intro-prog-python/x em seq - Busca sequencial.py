
''' dados como paremetros uma lista L e um numero real x devolve a posiçao que x ocorre ou none caso x nao esteja na lista

depois, usando a função anterior, escrever um programa q le uma sequencia de numeros reais e depois imprime a sewuencia eliminando os elementos repetidos
'''

def acha(seq, x):

    i=0
    while i < len(seq) and seq[i] !=x :
        i += 1

    if i == len (seq):  #percorri a seq inteira e não encontrei x
        return None
    else:
        return i

def main():
    n = int(input("Digite o tamanho da sequência: " ))

    lista = []
    for i in range (1,n+1):
        numero = float(input("Digite o %dº número da sequência: " %i))
        if acha(lista, numero) == None:
            lista.append (numero)

    print("A sequência de números sem repeticoes fica:", lista)



def acha2(seq,x):
    i=0
    while i < len(seq_ordenada) and seq_ordenada[i] < x:
        i += 1

    if i == len(seq) or seq_ordenada[i] != x:
        return None
    else:
        return i




main()
        

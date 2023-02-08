'''programa q dada uma frase, imprime a palavra mais longa nela, junto com seu comprimento'''

def main():

    frase = input('Digite, por favor, a frase desejada: ')
    separador = input('Qual seria o separador das palavras? ')

    palavra = ""
    maior_palavra = ""

    lista_palavras = separa(frase, str(separador))

    for palavra in frase:
        if len(palavra) >= len(maior_palavra):
            maior_palavra = palavra


    print('A maior palavra da frase é "%s", com %d letras.' %(maior_palavra, len(maior_palavra)))



def separa (texto,sep):
    palavra = ""
    lista = []

    for c in texto:
        if c == sep and palavra != "":
            lista.append(palavra)
            palavra = ""
        else:    #qualquer coisa que não é separador é considerada palavra
            palavra += c

    if palavra != "":
        return palavra
        

    

main() 

            

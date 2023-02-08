'''programa q dada uma frase, imprime a palavra mais longa nela, junto com seu comprimento'''

def main():

    frase = input('Digite, por favor, a frase desejada: ')

    palavra = ""
    maior_palavra = ""

    for c in frase:
        if "a" <= c <= "z" or "A" <= c <= "Z":  #verifica se c é uma letra 
            palavra += c
        else:     #ou um caractere qualquer  ( , . : ; $ ... # @ * )
            if len(palavra) >= len(maior_palavra):
                maior_palavra = palavra

            palavra = ""

    if len(palavra) >= len(maior_palavra):
        maior_palavra = palavra

    print('A maior palavra da frase é "%s", com %d letras.' %(maior_palavra, len(maior_palavra)))

main()
            

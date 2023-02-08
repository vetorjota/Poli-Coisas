'''programa q, dada uma frase, vai transformar tds as letras em minuscula e
depois em maiuscula'''

def main():
    frase = input("Digite uma frase:")
    frase_maiuscula = ""
    frase_minuscula = ""

    for caractere in frase:
        frase_maiuscula += maiuscula(caractere)
        frase_minuscula += minuscula(caractere)

    print (frase_maiuscula)
    print (frase_minuscula)



def maiuscula(c):
    if 'a' <= c <= 'z':   #a letra fica entre os extremos do alfabeto minúsculo
         c = chr(ord('A') + (ord(c) - ord('a')))

    return c

def minuscula(d):
    if 'A' <= d <= 'Z':
        d = chr(ord('a') + (ord(d) - ord('A')))

    return d


main()

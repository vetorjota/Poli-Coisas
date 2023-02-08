''' estudo de strings '''

def main():

    print('\n\n\t Contar palavras num texto:')
    
    narch = input('Digite o nome do aquivo contendo o texto ')
    arquivo = open((narch +'.txt') , 'r')
    word = input('Qual palavra você quer contar? ') 

    novo_arquivo = subst_pontuação(converte_min(arquivo.read()))
    lista_palavras = novo_arquivo.split()

    cont = 0
    for palavra in lista_palavras:
        if word == palavra:
            cont +=1

    print('A palavra %s aparece %d vezes no arquivo-texto %s' %(word, cont, narch))


    
    arquivo.close()


def converte_min(linha_palavras):

    nova_linha = ''
    for c in linha_palavras:
        if 'A' <= c <= 'Z':
            nova_linha += chr(ord('a') + ord(c) - ord('A'))
        else:
            nova_linha += c
            

    return nova_linha


def subst_pontuação(linha):

    nova_linha = ''
    pontuação = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for c in linha:
        if c not in pontuação:
            nova_linha += c

        else:
            nova_linha += ' '

    return nova_linha
            

main()








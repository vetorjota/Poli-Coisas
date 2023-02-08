'''lendo um poema'''


def main():

    nome_arquivo = input("Digite o nome do arquivo")

    arquivo = open(nome_arquivo,'r')

    cont_linha = 1

    for linha in arquivo:

        linha_sem_esp = linha.strip()
        print("Linha %d: %s" %(cont_linha,linha_sem_esp)

        cont_linha+=1

    arquivo.close()



main()

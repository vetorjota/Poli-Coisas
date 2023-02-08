'''lendo um poema'''


def main():


    abriu = False
    while not abriu:    

        nome_arquivo = input("Digite o nome do arquivo")

        try:
            arquivo = open(nome_arquivo, 'r')
        except FileNotFoundError:       #quando ocorre esta exceção
            print(nome_arquivo, 'não encontrado! Verifique se você digitou o nome corretamente!')
        else:     #quando o try é executado sem o que está no except, entra no else
            abriu = True



    cont_linha = 1

    for linha in arquivo:

        linha_sem_esp = linha.strip()
        print("Linha %d: %s" %(cont_linha,linha_sem_esp)

        cont_linha+=1

    arquivo.close()



main()

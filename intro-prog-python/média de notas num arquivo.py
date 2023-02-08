''' lista de alunos e notas
usando extenção csv para arquivos'''


def main():

    nome_arq = input('digite o nome do arquivo csv com os nomes e notas dos alunos: ')
    arquivo = open(nome_arq, 'r')

    contal = 0
    for registro_aluno in arquivo:    #para cada linha de aluno do arquivo
        
        lista_dados_aluno = registro_aluno.split(";") #cria lista de strings com os dados do aluno

        #calculando média das notas do aluno
        soma_nts_al = 0
        for i in range (1,len(lista_dados_aluno)):  #começa no 1 porque desconta o nome do aluno
            soma_nts_al += int(lista_dados_aluno[i])

        média_aluno = soma_nts_al / len(lista_dados_aluno) - 1   #tira um, pois um deles é o nome
        print ('Aluno: %s\t | Média: %f ' %(lista_dados_aluno[0],média_aluno))

        soma_media_turma += média_aluno
        contal +=1

    print('A média da turma é', soma_media_turma / contal)
            
        


main()

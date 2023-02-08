'''
Dado um número inteiro n>0, faça uma função molduras_concentricas (n, v1, v2) que gera uma matriz quadrada nxn 
preenchida com um padrão de modluras concêntricas alternando entre dois valores fornecidos v1 e v2.
'''

def cria_matriz (num_linhas, num_colunas, valor):
    matriz=[]

    for i in range(num_linhas):
        linha = []
        for j in range (num_colunas):
            linha.append(valor)
        matriz.append(linha)

    return matriz


def molduras_concentricas (n, v1,v2):



    M = cria_matriz(n,n,-1)

    for i in range (n):
        for j in range (n):
            dv = abs(i - n//2)  # distância vertical de posição (i,j) com relação ao centro
            dh = abs(j - n//2)  # distância horizontal de posição (i,j) com relação ao centro

            if dv > dh:
                maior_d = dv
            else:
                maior_d = dh

            if maior_d % 2 == 0:
                M[i][j] = v1
            else:
                M[i][j] = v2
            
    return M

def gravaPGM (nome_arquivo_sem_extensao, mat):
    arquivo = open(nome_arquivo_sem_extensao + ".pgm", "w")

    #indica que o arquivo é do tipo PGM(P2)
    arquivo.write("P2\n")
    #grava no arquivo dimensões de imagem (numero de colunas x numero de linhas)
    arquivo.write(str(len(mat[0])) + " " + str(len(mat)) + "\n")
    #maior intensidade de cor que a imagem conterá
    arquivo.write("255\n")

    for linha in mat:
        for cor in linha:
            arquivo.write(str(cor) + " ")
        arquivo.write("\n")
    
    arquivo.close()

def main():
    n = int(input("Digite o tamanho da imagem (número de linhas): "))
    nome_do_arquivo = input("Digite o nome do arquivo (sem extensão) da imagem a ser criada: ")
    mat = molduras_concentricas(n, 0, 255)
    gravaPGM(nome_do_arquivo, mat)

main()
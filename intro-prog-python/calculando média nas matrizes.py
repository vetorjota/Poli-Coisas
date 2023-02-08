''' esta fç vai calcular a media dos vizinhos e o numero k. vai aplicar k transformaçoes,
substituindo o valor da posição ao redor pelo da média das posiçoes ao redor.'''

def main():

    A = le_matriz()
    imprime_matriz(A)

    k= int(input('digite o valor de k --numero de transformações--:'))

    for cont in range (1,k+1):
        A = gera_matriz_media(A)
        print('A matriz A depois da %d-ésima transformação fica: ' %cont)
        imprime_matriz(A)


def gera_matriz_media(A):  #recebe a matriz A e gera uma nova matriz, com as médias

    Amedia = []

    for i in range (len(A)):    #percorre linhas de A
        Amedia.append ([])      # cria uma nova linha em Amédia
        for j in range (len(A[i])): #dentro de cada linha dde A, percorre os elementos
            Amedia[i].append(calcula_media(A,i,j))   #criando elemento i,j na matriz Amedia com a média dos valores ao redor da posição i,j na matriz A

            

def le_matriz():
    m=int(input('digite o numero de linhas da matriz'))
    n=int(input('digite o numero de colunas da matriz'))

    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            numero = int(input('digite o numero da posição (' + str(i+1) + ',' + str(j+1) + '):' ))
            mat[i].append(numero)     #acrescentando o valor na linha atual

    return mat
            


def calcula_media(mat,i,j):
    soma = 0
    num_vizinhos = 0

    for incremento_linha in range (-1,2):    # vai devolver -1, 0 e 1. é o vai acrescentar no i para acessar as posições desejadas.
        for incremento_coluna in range (-1,2):
            if 0 <= i+incremento_linha < len(mat) and 0 <= j+incremento_coluna < len(mat[i]):   #verifica se a posição está dentro da matriz 
                soma += mat[i+incremento_linha][j+incremento_coluna]    #oferece 9 posições incluindo o próprio valor
                num_vizinhos +=1

    soma = soma - mat [i][j]
    






def conta_bombas(matt,i,j):
    cont = 0

    if i>=1 :
        if matt [i-1][j] == -1:      #verifica se a posição logo abaixo contém bomba. é preciso, porém, ver SE a posição existe.
            cont +=1

        if j >= 1 and matt[i-1][j-1] == -1:      #verifica a posição diagonal superior esquerda
            cont+=1

        if j < len(matt[i])-1 and matt [i-1][j+1]== -1:      #verifica diagonal superior direita
            cont += 1

            

    if i < len(matt) - 1 :
        if matt[i+1][j] == -1:   #verifica a posição de cima. matriz é uma lista de linhas. len(mat) - 1 porque é a ultima linha menos uma posição
            cont +=1                           #se não, poderia verificar elementos que estariam além da borda da matriz.

        if j>=1 and matt[i+1][j-1] == -1:  #pos diagonal inferior esquerda, ela existindo
            cont +=1

        if j< len(matt[i])-1 and matt[i+1][j+1] == -1:
            cont +=1



    if j >=1 and matt[i][j-1] == -1: #verifica posição à esquerda, a menos que esteja falando da primeira coluna.
        cont +=1

    if j < len(matt[i]) - 1 and matt[i][j+1] == -1: 
        cont +=1


    return cont      #retorna, finalmente, o valor. pode-se ver que seu número máximo é 8


    
        




def imprime_matriz(mat):
    for i in range (len(mat)):
        for j in range (len (mat[i])):    #numero de colunas na linha atual
            print('%6f' %(mat[i][j]), end = " ")

        print()

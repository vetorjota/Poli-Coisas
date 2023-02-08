''' joguinho do campo minado '''

def main():
    campo_minado = le_matriz()
    imprime_matriz(campo_minado)


    for idelinha in range (len(campo_minado)):
        for jdecoluna in range (len(campo_minado[i])):
            if campo_minado[i][j] == 0:
                conta_bombas(campo_minado, idelinha, jdecoluna)


    print('a matriz com a contagem de bombas fica')
    imprime_matriz(campo_minado)

    

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


    #???????????      #retorna, finalmente, o valor. pode-se ver que seu número máximo é 8


    
        


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


def imprime_matriz(mat):
    for i in range (len(mat)):
        for j in range (len (mat[i])):    #numero de colunas na linha atual
            print('%6d' %(mat[i][j]) , end = " ")

        print()





main()


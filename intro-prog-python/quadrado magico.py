''' vamos ver se a matriz é um quadrado magico'''


def main():

    n=int(input("digite o numero de linhas ou colunas da matriz: "))
    A=[]

    for i in range (n):    #lê tal linha
        A.append ([])
        for j in range(n):
            numero = int(input("Digite um numero inteiro para a posição (%d,%d)" %(i+1,j+1)))
            A[i].append(numero)

    soma_referencia = 0
    for numero in A[0]:
        soma_referencia += numero


    quad_magico = True
    i=1
    while i<n and quad_magico:   #percorre linhas de A
        soma_linha = 0
        for numero in A[i]:
            soma_linha += numero

        if soma_linha != soma_referencia:
            quad_magico = False

        i+=1

    j=0
    while j < n and quad_magico:    #percorre colunas de A
        soma-coluna = 0
        for i in range(n):
            soma_coluna += A[i][j]

        if soma_coluna != soma_referencia:
            quad_magico = False

        j+=1

    soma_diagonal = 0
    soma_diag_sec = 0
    while k < n and quad_magico:
        soma_diagonal += A[k][k]
        soma_diag_sec += A[k][n-k-1]
        k+=1

    if soma_diagonal != soma_referencia:
        quad_magico = False


    if quad_magico:
        print("A matriz é um quadrado mágico.")

    else:
        print('não')

        


main()
        
        

def main ():
    n = int(input("Digite o número de linhas a ser impressa: "))
    pascal = []
    for j in range (n):
        linha = []
        for k in range (j+1):
            linha.append(binomio(j,k))
        pascal.append(linha)

    imprime(pascal)
         
 
def binomio (n, k):
    nfat = kfat = nkfat = 1
    for i in range (2, n+1):
        nfat *= i
        if i <= k:
            kfat *= i
        if i < n - k + 1:
            nkfat *= i

        print(i)
        print('nfat:',nfat)
        print('kfat:',kfat)
        print('nkfat:',nkfat)
    bin = (nfat)/(kfat*nkfat)
    return bin


def imprime(m):

    for i in range(len(m)):
        for c in range (len(m[i])):
            print (m[i][c], end = " ")
        print('\n')

main()

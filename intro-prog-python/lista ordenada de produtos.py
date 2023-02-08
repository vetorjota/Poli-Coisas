
''' a) funcao q dados como parametro uma lista de registros de produtos em ordem crescente por nome e um novo
registro de produto, insere o novo registro na lista mantendo a ordenaçao. um registro de produto está na forma [<nome do produto>, <cor>, <preço>];

b) escrever programa que leia sequencia de registros de produtos e depois exibe em ordem crescente de nome de produto.
'''


def insere_ordenado(lista_produtos, novo_produto):

    i = 0
    n = len(lista_produtos)
    while i < n and lista_produtos [i][0] < novo_produto[0]:  #primeiro acessamos o nome do produto(coluna 0) dentro de cada linha i(cada produto)da matriz dos produtos
        i += 1

    lista_produtos.append([])   #representando produto q não tem nada, apenas acrescentando uma posição na lista
    
    k = n - 1    #queremos pegar a última posição da lista, por isso diminuímos 1.

    while k > i:
        lista_produtos[k] = lista_produtos[k-1]
        k -= 1

    lista_produtos[i] = novo_produto




def main():

    n = int(input('Digite o número de produtos que serão fornecidos: '))

    prods = []

    for i in range(n):
        print('***PRODUTO Nº %d ***' %(i+1))
        produto = []
        produto.append(input('Digite o nome do produto: '))
        produto.append(input('Digite a cor do produto: '))
        produto.append(float(input('Digite o valor do produto: '))

        insere_ordenado(prods, produto)

    for produto in prods:    #for i in range (len(prods)
        print(produto)


main()
        
    

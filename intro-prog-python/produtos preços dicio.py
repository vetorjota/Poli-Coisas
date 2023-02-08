
'''produtos'''

def main():
    nome_arq = input('digite o nome do arquivo com os preços dos produtos:   ')
    arq = open(nome_arq, "r")
    preços_prods = {} #criando dicionario vazio para armazenar os pares (produto : preço)

    for linha in arq:
        print (linha)
        valores = linha.strip().split()  #o split separa a linha a cada intervalo de espaço " ". se fosse ',', seria split(,)
        produto = valores[1]
        preço = float(valores [2])

        if produto not in preços_prods or preços_prods[produto] > preço:
            preços_prods[produto] = preço

            
    for produto in preços_prods:
        print('Produto: %s \t\tMenor preço: %.2f' %(produto, preços_prods[produto]))

    for produto in preços_prods.keys():
        print('Produto: %s \t\tMenor preço: %.2f' %(produto, preços_prods[produto]))

    for value in preços_prods.values():
        print(value)

    for (x,y) in preços_prods.items():
        print(x,y)

    print(list(preços_prods))

main()
        

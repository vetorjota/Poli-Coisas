def identificar_cadeias_horizontais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias horizontais de 3 ou mais gemas. Cada cadeia é
    representada por uma lista `[linha, coluna_i, linha, coluna_f]`, onde:

    - `linha`: o número da linha da cadeia
    - `coluna_i`: o número da coluna da gema mais à esquerda (menor) da cadeia
    - `coluna_f`: o número da coluna da gema mais à direita (maior) da cadeia

    Não modifica o tabuleiro.
    '''
    cadeias = []
    for i in range (len(tabuleiro)):
        qts_iguais = 0
        j = 0
        possivel_cadeia = []
        for j in range ( len(tabuleiro[0]) - 1 ):

                if tabuleiro [i][j] == tabuleiro [i][j+1]:
                    é_cadeia = True
                    qts_iguais += 1
                    possivel_cadeia.append (i)
                    possivel_cadeia.append (j)

                    k = j
                    while tabuleiro [i][k] == tabuleiro [i][k+1] and k+1 < (len(tabuleiro[0])) - 1:
                        k+=1
                        qts_iguais +=1

                    
                    if qts_iguais >= 3:
                        possivel_cadeia.append (i)
                        possivel_cadeia.append (k+1)
                        cadeias.append (possivel_cadeia)
                        possivel_cadeia = []
                        

                '''
                elif tabuleiro[i][j] != tabuleiro [i][j+1]:
                    possivel_cadeia.append (i)
                    possivel_cadeia.append (j)
                    if qts_iguais >= 3:
                        cadeias.append (possivel_cadeia)
                        possivel_cadeia = []
                    else:
                        possivel_cadeia = []

                if j+1 == len(tabuleiro[0]) - 1 :  #fim da linha,última coluna da linha
                    if tabuleiro [i][j] == tabuleiro [i][j+1]:
                        é_cadeia = True
                        qts_iguais += 1
                        possivel_cadeia.append (i)
                        possivel_cadeia.append (j)

                    if qts_iguais >= 3:
                        possivel_cadeia.append (i)
                        possivel_cadeia.append (j)
                        cadeias.append (possivel_cadeia)
                        possivel_cadeia = []
                    else:
                        possivel_cadeia = []
                        qts_iguais = 0


------------------------------



                    
                    while k < len(tabuleiro[0]-1) and é_cadeia:
                        if tabuleiro[i][j] == tabuleiro[i][j+1]:
                            qts_iguais += 1

                            
                        elif tabuleiro [i][j] != tabuleiro [i][j+1] or j+1 == len(tabuleiro[0])- 1 :
                            possivel_cadeia.append (i)
                            possivel_cadeia.append (k-1)

                            if qts_iguais >= 3:
                                cadeias.append (possivel_cadeia)
                                possivel_cadeia = []
                            else:
                                é_cadeia = False
                                possivel_cadeia = []
                                qts_iguais = 0
                    
                        k += 1
                    '''

                        
                

    return cadeias


def exibir (tabuleiro): 
    ''' (matrix) -> None

    Exibe o tabuleiro.
    '''

    #contador de colunas
    num_col=0
    for y in range (len(tabuleiro[0])):
        num_col += 1

    #imprime índice da coluna    
    print('    ',end="")
    for i in range (num_col):
        print ((str(i)), end=" ")

    print()
    
    print ('  +',end = "")    #margem superior
    for i in range (num_col *2 + 1):
        print('-', end = "")
    print ('+')

    #imprimindo matriz do tabuleiro
    for i in range ((len(tabuleiro))):
        for j in range (-1,(len(tabuleiro[i]))):
            if j == -1:
                print (str(i),'|',end=" ")
            elif j < (len(tabuleiro[i])):
                print (('%1c' %(tabuleiro[i][j])),end=" ")
            if j == (len(tabuleiro[i])-1):
                print('|')


    print ('  +',end = "")     #aqui começa a margem inferior
    for i in range (num_col *2 + 1):
        print('-', end = "")
    print ('+')




exibir([['B', 'F', 'C', 'F', 'G'], ['A', 'B', 'E', 'B', 'B'], ['G', 'G', 'G', 'E', 'D'], ['A', 'A', 'C', 'E', 'D'], ['A', 'C', 'E', 'C', 'F'], ['A', 'E', 'C', 'G', 'E'], ['B', 'G', 'E', 'E', 'E'], ['C', 'D', 'A', 'E', 'G'], ['D', 'C', 'E', 'B', 'C'], ['B', 'B', 'G', 'B', 'A']])


print(identificar_cadeias_horizontais([['B', 'F', 'C', 'F', 'G'], ['A', 'B', 'E', 'B', 'B'], ['G', 'B', 'G', 'E', 'D'], ['A', 'A', 'C', 'E', 'D'], ['A', 'C', 'E', 'C', 'F'], ['A', 'E', 'C', 'G', 'E'], ['B', 'G', 'E', 'E', 'E'], ['C', 'D', 'A', 'E', 'G'], ['D', 'C', 'E', 'B', 'C'], ['B', 'B', 'G', 'B', 'A']]))

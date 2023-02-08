"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
  DECLARO QUE SOU A ÚNICA PESSOA AUTORA E RESPONSÁVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E, PORTANTO, NÃO CONSTITUEM ATO DE DESONESTIDADE ACADÊMICA,
  FALTA DE ÉTICA OU PLÁGIO.
  DECLARO TAMBÉM QUE SOU A PESSOA RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE NÃO DISTRIBUÍ OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Júlia Morone Drummond Alves
  NUSP : 10355120
  Turma: 2 - 06
  Prof.: Kelly Rosa Braghetto

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.

  Não utilizei referências além do meu caderno de anotações nas aulas da
  professora Kelly Rosa Braghetto.
  
"""
# ======================================================================
#
#   FUNÇÕES FORNECIDAS: NÃO DEVEM SER MODIFICADAS
#
# ======================================================================
import random
random.seed(0)

def main():
    '''
    Esta é a função principal do seu programa. Ela contém os comandos que
    obtêm os parâmetros necessários para criação do jogo (número de linhas,
    colunas e cores), e executa o laço principlal do jogo: ler comando,
    testar sua validade e executar comando.

    ******************************************************
    ** IMPORTANTE: ESTA FUNÇÃO NÃO DEVE SER MODIFICADA! **
    ******************************************************
    '''
    print()
    print("=================================================")
    print("             Bem-vindo ao Gemas!                 ")
    print("=================================================")
    print()

    pontos = 0
    # lê parâmetros do jogo
    num_linhas = int(input("Digite o número de linhas [3-10]: ")) # exemplo: 8
    num_colunas = int(input("Digite o número de colunas [3-10]: ")) # exemplo: 8
    num_cores = int(input("Digite o número de cores [3-26]: ")) # exemplo: 7
    # cria tabuleiro com configuração inicial
    tabuleiro = criar (num_linhas, num_colunas)
    completar (tabuleiro, num_cores)
    num_gemas = eliminar (tabuleiro)
    while num_gemas > 0:
        deslocar (tabuleiro)
        completar (tabuleiro, num_cores)
        num_gemas = eliminar (tabuleiro)
    # laço principal do jogo
    while existem_movimentos_validos (tabuleiro): # Enquanto houver movimentos válidos...
        exibir (tabuleiro)
        comando = input("Digite um comando (perm, dica, sair ou ajuda): ")
        if comando == "perm":
            linha1 = int(input("Digite a linha da primeira gema: "))
            coluna1 = int(input("Digite a coluna da primeira gema: "))
            linha2 = int(input("Digite a linha da segunda gema: "))
            coluna2 = int(input("Digite a coluna da segunda gema: "))
            print ()
            valido = trocar ( linha1, coluna1, linha2, coluna2, tabuleiro)
            if valido:
                num_gemas = eliminar (tabuleiro)
                total_gemas = 0
                while num_gemas > 0:
                    # Ao destruir gemas, as gemas superiores são deslocadas para "baixo",
                    # criando a possibilidade de que novas cadeias surjam.
                    # Devemos então deslocar gemas e destruir cadeias enquanto houverem.
                    deslocar (tabuleiro)
                    completar (tabuleiro, num_cores)
                    total_gemas += num_gemas
                    print("Nesta rodada: %d gemas destruidas!" % num_gemas )
                    exibir (tabuleiro)
                    num_gemas = eliminar (tabuleiro)
                pontos += total_gemas
                print ()
                print ("*** Você destruiu %d gemas! ***" % (total_gemas))
                print ()
            else:
                print ()
                print ("*** Movimento inválido! ***")
                print ()
        elif comando == "dica":
            pontos -= 1
            linha, coluna = obter_dica (tabuleiro)
            print ()
            print ("*** Dica: Tente permutar a gema na linha %d e coluna %d ***" % (linha, coluna))
            print ()
        elif comando == "sair":
            print ("Fim de jogo!")
            print ("Você destruiu um total de %d gemas" % (pontos))
            return
        elif comando == "ajuda":
            print("""
============= Ajuda =====================
perm:  permuta gemas
dica:  solicita uma dica (perde 1 ponto)
sair:  termina o jogo
=========================================
                  """)
        else:
            print ()
            print ("*** Comando inválido! Tente ajuda para receber uma lista de comandos válidos. ***")
            print ()
    print("*** Fim de Jogo: Não existem mais movimentos válidos! ***")
    print ("Você destruiu um total de %d gemas" % (pontos))

def completar (tabuleiro, num_cores):
    ''' (matrix, int) -> None

    Preenche espaços vazios com novas gemas geradas aleatoriamente.

    As gemas são representadas por strings 'A','B','C',..., indicando sua cor.
    '''
    alfabeto = ['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num_linhas = len (tabuleiro)
    num_colunas = len (tabuleiro[0])
    for i in range (num_linhas):
        for j in range (num_colunas):
            if tabuleiro[i][j] == ' ':
                gema = random.randrange (num_cores)
                tabuleiro[i][j] = alfabeto[gema]


# ======================================================================
#
#   FUNÇÕES A SEREM IMPLEMENTADAS POR VOCÊ
#
# ======================================================================

def criar (num_linhas, num_colunas):
    ''' (int,int) -> matrix

    Cria matriz de representação do tabuleiro e a preenche com
    espaços vazios representados por ' '.

    Retorna a matriz criada.
    '''
    matriz = []

    for i in range (num_linhas):
        matriz.append ([])
        for j in range (num_colunas):
            matriz[i].append (' ')


    return matriz

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
                
    

def trocar (linha1, coluna1, linha2, coluna2, tabuleiro):
    ''' (int,int,int,int,matrix) -> Bool

    Permuta gemas das posições (linha1, coluna1) e (linha2, coluna2) caso
    seja válida (isto é, gemas são adjacentes e geram cadeias), caso contrário
    não altera o tabuleiro.

    Retorna `True` se permutação é válida e `False` caso contrário.
    '''

    #trocá-las se forem adjacentes e verificar se geram cadeias; caso não gerem, destroca

    #verificar se são adjacentes verticais:
    adj_v = False
    if coluna1 == coluna2 and (linha1 == linha2 + 1 or linha1 == linha2 -1) :
        adj_v = True

    #verificar se são adjacentes horizontais:
    adj_h = False
    if linha1 == linha2 and (coluna1 == coluna2 + 1 or coluna1 == coluna2 -1) :
        adj_h = True


    qts_iguais = 0 #contador de gemas iguais



    
    if adj_h or adj_v:     #verifica adjascência para trocar
        aux1 = tabuleiro[linha1][coluna1]
        aux2 = tabuleiro[linha2][coluna2]
        tabuleiro[linha1][coluna1] = tabuleiro[linha2][coluna2]
        tabuleiro [linha2][coluna2] = aux1

        #verificar se, trocando essas posições, elas gerariam alguma cadeia na horizontal, se não gerarem, a troca será desfeita

        if len(identificar_cadeias_horizontais(tabuleiro) ) != 0  or  len(identificar_cadeias_verticais(tabuleiro)) != 0 :    #verificando se formou alguma cadeia
            return True

        else:
            tabuleiro [linha1][coluna1] = aux1
            tabuleiro [linha2][coluna2] = aux2
            return False


    else:    #se não forem adjascentes, a troca não pode ocorrer
        return False
    
    

    


        
        
    
        '''for j in range (coluna1,(len(tabuleiro))):
            while tabuleiro [linha1][coluna1] == tabuleiro[linha1][j] or tabuleiro [linha2][coluna2] == tabuleiro[linha2][j]:
                qts_iguais += 1
                if qts_iguais == 3:
                    return True'''



        
        


    #if adj_v and ( identificar_cadeias_horizontais(tabuleiro)) [1] == :


    #if identificar_cadeias_horizontais(tabuleiro)[0] == linha1:
    


    
    


def eliminar (tabuleiro):
    ''' (matrix) -> int

    Elimina cadeias de 3 ou mais gemas, substituindo-as por espaços (' ').

    Retorna número de gemas eliminadas.
    '''
    num_eliminados = 0

    '''for i in range (len(tabuleiro)):
        for j in range (len(tabuleiro[0])):'''


    if identificar_cadeias_horizontais(tabuleiro) != []:    
        for cadeia in identificar_cadeias_horizontais(tabuleiro):
            num_eliminados += eliminar_cadeia(tabuleiro,cadeia)   #somando os pontos advindos da eliminação de uma cadeia horizontal

    if identificar_cadeias_verticais(tabuleiro) != []:
        for cadeia in identificar_cadeias_verticais(tabuleiro):
            num_eliminados += eliminar_cadeia(tabuleiro,cadeia)   #somando pontos advindos da eliminação de uma cadeia vertical
        

    
    '''
    if identificar_cadeias_horizontais(tabuleiro) != []:
        li = identificar_cadeias_horizontais(tabuleiro) [0]
        ci = identificar_cadeias_horizontais(tabuleiro) [1]
        lf = identificar_cadeias_horizontais(tabuleiro) [2]
        cf = identificar_cadeias_horizontais(tabuleiro) [3]
        
        num_eliminados = lf - li + 1
    
        for i in range(li,lf+1):
            if tabuleiro [i][ci] == " ":
                num_eliminados -= 1

        eliminar_cadeia(tabuleiro,[li,ci,lf,cf])
        


    if identificar_cadeias_verticais(tabuleiro) != []:
        
        li = identificar_cadeias_verticais(tabuleiro) [0]
        ci = identificar_cadeias_verticais(tabuleiro) [1]
        lf = identificar_cadeias_verticais(tabuleiro) [2]
        cf = identificar_cadeias_verticais(tabuleiro) [3]

        num_eliminados = cf - ci + 1

        for j in range(ci,cf+1):    
            if tabuleiro [li][j] == " ":  #cadeia vertical tem elementos que já foram eliminados no laço anterior
                num_eliminados -= 1

        eliminar_cadeia(tabuleiro,[li,ci,lf,cf])

    '''


    '''
    for j in range (ci,cf+1):
        if tabuleiro [li][j] == " ":
            num_eliminados -= 1
        tabuleiro[li][j] = " "
        num_eliminados += 1
    '''
    

    return num_eliminados

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
        k = 1
        j = 0
        possivel_cadeia = []
        while k < len(tabuleiro[0]) and j < len(tabuleiro[0]):

                if tabuleiro [i][j] == tabuleiro [i][k]:
                    é_cadeia = True
                    qts_iguais += 1
                    possivel_cadeia.append (i)
                    possivel_cadeia.append (j)
   
                    while k < len(tabuleiro[0]) and é_cadeia:
                        if tabuleiro[i][j] == tabuleiro[i][k]:
                            qts_iguais += 1

                        elif tabuleiro [i][j] != tabuleiro [i][k] or k == len(tabuleiro[0])- 1 :
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


                k += 1
                j += 1        
                

    return cadeias


def identificar_cadeias_verticais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias verticais de 3 ou mais gemas. Cada cadeia é
    representada por uma lista `[linha_i, coluna, linha_f, coluna]`, onde:

    - `linha_i`: o número da linha da gemas mais superior (menor) da cadeia
    - `coluna`: o número da coluna das gemas da cadeia
    - `linha_f`: o número da linha mais inferior (maior) da cadeia

    Não modifica o tabuleiro.
    '''
    
    '''    while i > 0:
        for j in range (len(tabuleiro[i]),0,-1):
            for decremento in range (len(tabuleiro)):
                if tabuleiro [i][j] == tabuleiro [i-decremento][j] and tabuleiro [i-decremento][j] == tabuleiro[i-2][j]:
                    if tabuleiro [i][j] == tabuleiro [i-3][j]:      #aqui é preciso fazer mais verificações, se não
                        print(daffuq)#o i - 3 ou etc pode dar erro devido à posição não existente.

        i -= 1'''

    cadeias = []
    for i in range (len(tabuleiro)):
        x = 1
        qts_iguais = 0
        k = 1
        j = 0
        possivel_cadeia = []
        while k < len(tabuleiro) and j < len(tabuleiro[0]):

                x = 1
                if tabuleiro [i][j] == tabuleiro [k][j]:
                    qts_iguais += 1
                    possivel_cadeia.append (i)
                    possivel_cadeia.append (j)
   
                    while k < len(tabuleiro) and x == 1:
                        if tabuleiro[i][j] == tabuleiro[k][j]:
                            qts_iguais += 1

                        elif tabuleiro [i][j] != tabuleiro [k][j] or k == len(tabuleiro)- 1 :
                            possivel_cadeia.append (k-1)
                            possivel_cadeia.append (j)

                            if qts_iguais >= 3:
                                cadeias.append (possivel_cadeia)
                                possivel_cadeia = []
                            else:
                                x = -1
                                possivel_cadeia = []

                        k += 1


                #k += 1
                j += 1

    print(tabuleiro) #RETIRAR

    return cadeias

def eliminar_cadeia (tabuleiro, cadeia):
    ''' (matrix,list) -> int

    Elimina (substitui pela string espaço `" "`) as gemas compreendidas numa cadeia,
    representada por uma lista `[linha_inicio, coluna_inicio, linha_fim, coluna_fim]`,
    tal que:

    - `linha_i`: o número da linha da gema mais superior (menor) da cadeia
    - `coluna_i`: o número da coluna da gema mais à esquerda (menor) da cadeia
    - `linha_f`: o número da linha mais inferior (maior) da cadeia
    - `coluna_f`: o número da coluna da gema mais à direita (maior) da cadeia

    Retorna o número de gemas eliminadas.
    '''
    num_eliminados = 0


    li = cadeia[0]    #linha inicial
    ci = cadeia[1]    #coluna inicial
    lf = cadeia[2]    #linha final
    cf = cadeia[3]    #coluna final




    if li == lf:             #cadeia é horizontal
        num_eliminados = cf - ci + 1
        for coluna in range(ci,cf+1):
            if tabuleiro [li][coluna] == " ":    #interseção de cadeias ver e hor
                num_eliminados -= 1
            tabuleiro[li][coluna] = " "

    elif ci == cf:           #cadeia é vertical
        num_eliminados = lf - li + 1
        for linha in range(li,lf+1):
            if tabuleiro [linha][cf] == " ":    #interseção de cadeias ver e hor
                num_eliminados -= 1
            tabuleiro[linha][cf] = " "





    return num_eliminados


def deslocar (tabuleiro):
    ''' (matrix) -> None

    Desloca gemas para baixo deixando apenas espaços vazios sem nenhuma gema acima.
    '''




    #horizontal

    for k in range (len(identificar_cadeias_horizontais(tabuleiro))):
        for j in range (identificar_cadeias_horizontais(tabuleiro)[k][1],identificar_cadeias_horizontais(tabuleiro)[k][3]+1): #j entre colunas inicial e final da cadeia
            print("mais uma na hor")

    for k in range (len(identificar_cadeias_verticais(tabuleiro))):
        for j in range (identificar_cadeias_verticais(tabuleiro)[k][0],identificar_cadeias_verticais(tabuleiro)[k][2]+1): #j entre colunas inicial e final da cadeia
            print("mais uma na ver")

    for i in range (len(tabuleiro)-1,-1,-1):
        for j in range (len(tabuleiro[0])-1,-1,-1):
            if tabuleiro[i][j] == " ":
                deslocar_coluna(tabuleiro,j)
                
    


    
    print("sos deslocar")
                


def deslocar_coluna ( tabuleiro, i ):
    ''' (matrix, int) -> None

    Desloca as gemas na coluna i para baixo, ocupando espaços vazios.
    '''
    colunai = []    #lista para armazenar elementos não "vazios" da coluna
    for linha in range ((len(tabuleiro)-1),-1,-1):
        if tabuleiro[linha][i] != " ":
            append.colunai (tabuleiro[linha][i])
        else:
            print(colunai)

    substituicoes = len(tabuleiro[0]) - len(colunai)
    for linha in range (len(tabuleiro)-1,-1,-1):
        for k in range (len(colunai)):
            tabuleiro[linha][i] = colunai[k]

    for linha in range (len(tabuleiro)):
        while substituicoes <= 0 :
            tabuleiro[linha][i] = " "
            substituicoes -= 1

    

                   
    print("ok função deslocar coluna")

def existem_movimentos_validos (tabuleiro):
    '''(matrix) -> Bool

    Retorna True se houver movimentos válidos, False caso contrário.
    '''

    if obter_dica(tabuleiro) == (-1,-1):
        return False

    else:
        return True


def obter_dica (tabuleiro):
    '''(matrix) -> int,int

    Retorna a posição (linha, coluna) de uma gema que faz parte de uma
    permutação válida.

    Se não houver permutação válida, retorne -1,-1.
    '''
    linha = -1
    coluna = -1


    if len(identificar_cadeias_horizontais(tabuleiro)) != 0:
        for k in range (len(identificar_cadeias_horizontais(tabuleiro))):
            for l1 in range (identificar_cadeias_horizontais(tabuleiro) [k][0],(identificar_cadeias_horizontais(tabuleiro) [k][2]) +1):
                for c1 in range (identificar_cadeias_horizontais(tabuleiro) [k][1], (identificar_cadeias_horizontais(tabuleiro) [k][3]) +1):
                    for i in range (len(tabuleiro)):
                        for j in range (len(tabuleiro[0])):
                            
                            if trocar(l1,c1,i,j,tabuleiro):
                                linha = i
                                coluna = j
                                trocar(i,j,l1,c1,tabuleiro)


    if len(identificar_cadeias_verticais(tabuleiro)) != 0:
        for k in range (len(identificar_cadeias_horizontais(tabuleiro))):
            for l1 in range (identificar_cadeias_verticais(tabuleiro) [k][0],(identificar_cadeias_verticais(tabuleiro) [k][2]) +1):
                for c1 in range (identificar_cadeias_verticais(tabuleiro) [k][1], (identificar_cadeias_verticais(tabuleiro) [k][3]) +1):
                    for i in range (len(tabuleiro)):
                        for j in range (len(tabuleiro[0])):
                            
                            if trocar(l1,c1,i,j,tabuleiro):
                                linha = i
                                coluna = j
                                trocar(i,j,l1,c1,tabuleiro)
                                

    return linha, coluna


main()

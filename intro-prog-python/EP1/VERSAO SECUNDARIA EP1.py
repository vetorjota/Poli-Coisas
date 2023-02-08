
'''falta cabeçalho, esta não é a versão oficial'''



# ======================================================================
#
#   M A I N 
#
# ======================================================================
def main():

    print()
    print("=================================================")
    print("         Bem-vindo ao Jogo da Cobrinha!          ")
    print("=================================================")
    print()
    
    nlinhas = int(input('Número de linhas do tabuleiro : '))
    ncols   = int(input('Número de colunas do tabuleiro: '))
    x0      = int(input('Posição x inicial da cobrinha : '))
    y0      = int(input('Posição y inicial da cobrinha : '))
    t       = int(input('Tamanho da cobrinha           : '))

    # Verifica se corpo da cobrinha cabe na linha do tabuleiro,
    # considerando a posição inicial escolhida para a cabeça
    if x0 - (t - 1) < 0:
        # Não cabe
        print()
        print("A COBRINHA NÃO PODE FICAR NA POSIÇÃO INICIAL INDICADA")
        
    else:

        ''' Inicia a variável d indicando nela que t-1 partes do corpo
            da cobrinha estão inicialmente alinhadas à esquerda da cabeça.
            Exemplos:
               se t = 4, então devemos fazer d = 222
               se t = 7, então devemos fazer d = 222222
        '''
        d = 0
        i = 1
        while i <= t-1: 
            d = d * 10 + 2
            i = i + 1
        
        # Laço que controla a interação com o jogador
        direcao = 1
        while direcao != 5:
            # mostra tabuleiro com a posição atual da cobrinha
            imprime_tabuleiro(nlinhas, ncols, x0, y0, d)
            
            # lê o número do próximo movimento que será executado no jogo
            print("1 - esquerda | 2 - direita | 3 - cima | 4 - baixo | 5 - sair do jogo")
            direcao = int(input("Digite o número do seu próximo movimento: "))
            
            if direcao != 5:
                # atualiza a posição atual da cobrinha
                x0, y0, d = move(nlinhas, ncols, x0, y0, d, direcao)

    print()        
    print("Tchau!")
    

# ======================================================================

def num_digitos(n):
     
    contdigitos=0
    
    while n/10 !=0:
        contdigitos += 1
        n //= 10


    if contdigitos == 0: #Para o caso de n ser 0, a função não devolver que ele possui 0 dígito
        contdigitos = 1
        

    return contdigitos
    """ (int) -> nt

    Devolve o número de dígitos de um número.

    ENTRADA
    - n: número a ser verificado 

    """

    

 
# ======================================================================
def pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):
    """(int, int, int, int, int, int, int) -> bool

    Devolve True se alguma parte da cobra ocupa a posição (x,y) e
    False no caso contrário.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x, y: posição a ser testada
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
    
    """

    # Escreva sua função a seguir e corrija o valor devolvido no return
    
    D = num_digitos(d)
    i=1


    
    while i < D :
        if d%10 == 1:
            if x == x0 + 1 :
                return True
            else:
                return False
        

        if d%10 == 2:
            if x == x0 - 1 :
                return True
            else:
                return False

        if d%10 == 3:
            if y == y0 + 1 :
                return True
            else:
                return False

        if d%10 == 4:
            if y == y0 - 1 :
                return True
            else:
                return False
            
        i+=1

    if x == x0 and y == y0:
        return True
    
        
        

    
    
    


# ======================================================================
def imprime_tabuleiro(nlinhas, ncols, x0, y0, d):
    """(int, int, int, int, int, int)

    Imprime o tabuleiro com a cobra.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
         
    """

    # Escreva sua função a seguir
    print("ESTA FUNÇÃO FOI reELABORADA ! FASE DE TESTES FINAIS")

    linhas_impressas = 0   #representa o "y"
    col_impressas = 0      #representa o "x"
    print((ncols+2)*'#')
    numd = num_digitos(d)

                    
    
    while linhas_impressas < y0:
        print('#', end="")
        while col_impressas < ncols:
            if pos_ocupada(nlinhas,ncols,col_impressas,linhas_impressas,x0,y0,d):
                print ('*',end="") """ outra possibilidade sem sentido seria
                                        while col_impressas != x0:
                                            print ('*',end="")
                                            col_impressas +=1
                                        if col_impressas == x0:
                                            print("C",end="")
                                            col_impressas+=1"""
                
            else:
                print(".",end="")
            col_impressas +=1
            
        print('#')
        linhas_impressas +=1
        col_impressas = 0

    col_impressas = 0 
    if linhas_impressas == y0:
        print('#',end ="")

        while col_impressas < ncols:
            if pos_ocupada(nlinhas,ncols,col_impressas,linhas_impressas,x0,y0,d):
                while col_impressas != x0:
                    print ('*',end="")
                    col_impressas +=1
                if col_impressas == x0:
                    print("C",end="")
                    col_impressas+=1

            else:
                print(".",end="")
                col_impressas +=1
            
            
        
        print('#')
        linhas_impressas +=1


    col_impressas=0
    while linhas_impressas < nlinhas:
        print('#',end="")
        while col_impressas < ncols:
            if pos_ocupada(nlinhas,ncols,col_impressas,linhas_impressas,x0,y0,d):
                print ('*',end="")

            else:
                print(".",end="")
            col_impressas +=1

        linhas_impressas +=1
        col_impressas=0
        print('#')



    print((ncols+2)*'#')
    


# ======================================================================
def move(nlinhas, ncols, x0, y0, d, direcao):
    """(int, int, int, int, int, int) -> int, int, int

    Move a cobra na direção dada.    
    A função devolve os novos valores de x0, y0 e d (nessa ordem).
    Se o movimento é impossível (pois a cobra vai colidir consigo mesma ou
    com a parede), então a função devolve os antigos valores e imprime a
    mensagem apropriada: "COLISÃO COM SI MESMA" ou "COLISÃO COM A PAREDE"

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
    - direcao: direção na qual a cabeça deve ser movida
    
    """
    
    # Escreva sua função a seguir e corrija o valor devolvido no return

    D = num_digitos(d)
    if direcao == 2:
        if x0 == (ncols-1): #colisão com parede direita
            print("COLISÃO COM A PAREDE!") 
            return x0,y0,d
        
        elif pos_ocupada(nlinhas,ncols,col_impressas,linhas_impressas,x0,y0,d):
            print("COLISÃO COM SI MESMA!")

        else:
            x0 += 1
            d= (d -((d//10**(D - 1))*10**(D -1))) * 10 + direcao #operações para atualizar a variável d
            return x0, y0, d
            

    elif direcao == 1:
        if x0 == 0: #colisão com parede esquerda
            print("COLISÃO COM A PAREDE!")
            return x0,y0,d
        
        elif pos_ocupada(nlinhas,ncols,col_impressas,linhas_impressas,x0,y0,d):
            print("COLISÃO COM SI MESMA!")

        else:
            x0 -= 1
            d = (d -((d//10**(D - 1))*10**(D -1))) * 10 + direcao
            return x0, y0, d

    elif direcao == 3:
        if y0 == 0: #colisão com parede superior
            print("COLISÃO COM A PAREDE!")
            return x0,y0,d

        elif pos_ocupada(nlinhas,ncols,col_impressas,linhas_impressas,x0,y0,d):
            print("COLISÃO COM SI MESMA!")
        
        else:
            y0 -= 1
            d = (d -((d//10**(D - 1))*10**(D -1))) * 10 + direcao
            return x0, y0, d


    elif direcao == 4:
        if y0 == (nlinhas-1): #colisão com parede inferior
            print("COLISÃO COM A PAREDE!")
            return x0,y0,d

        elif pos_ocupada(nlinhas,ncols,col_impressas,linhas_impressas,x0,y0,d):
            print("COLISÃO COM SI MESMA!")

        else:
            y0 +=1
            d = (d -((d//10**(D - 1))*10**(D -1))) * 10 + direcao
            return x0, y0, d

    
    
    print("Vixe! Ainda não terminei a função move()!")

    return x0, y0, d

# ======================================================================
main()     

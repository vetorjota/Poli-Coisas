def num_digitos(n):
     
    contdigitos=0 
    
    while n/10 !=0:
        contdigitos= contdigitos+ 1
        n//=10


    if contdigitos ==0: #Para o caso de n ser 0, a função não devolver que ele possui 0 dígito
        contdigitos =1
        

    return contdigitos

def imptab(nlinhas, ncols, x0, y0, d):
    """(int, int, int, int, int, int)

    Imprime o tabuleiro com a cobra.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
         
    """

    # Escreva sua função a seguir
    print("ESTA FUNÇÃO ESTÁ SENDO ELABORADA! FASE DE TESTES FINAIS")

    linhas_impressas=0
    print((ncols+2)*'#')
    numd = num_digitos(d)
                    
    

    while linhas_impressas < y0:
        print('#'+ncols*'.'+'#')
        linhas_impressas +=1

    if linhas_impressas == y0:
        print('#'+(x0-numd)*'.',end="")
        print(numd*'*',end="")
        print('C',end="")
        print((ncols-x0-1)*'.'+'#')
        linhas_impressas +=1

    while linhas_impressas < nlinhas:
        print('#'+ncols*'.'+'#')
        linhas_impressas +=1



    print((ncols+2)*'#')
    

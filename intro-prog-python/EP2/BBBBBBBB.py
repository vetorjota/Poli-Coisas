



def deslocar_coluna ( tabuleiro, i ):
    ''' (matrix, int) -> None

    Desloca as gemas na coluna i para baixo, ocupando espaços vazios.
    '''
    subst = 0
    for linha in range ((len(tabuleiro)-1),-1, -1):
        if tabuleiro [linha][i] == " ":  #preciso descer todos os elementos:if ou while? 
            for k in range ((len(tabuleiro)-2),0,-1):
                tabuleiro [linha][i] = tabuleiro [k][i]
                subst += 1
                print(tab)

    while subst >= 0:
        for k in range (len(tabuleiro)):
            tabuleiro[k][i] = " "
            subst -= 1


                   
    print("ok função deslocar coluna")



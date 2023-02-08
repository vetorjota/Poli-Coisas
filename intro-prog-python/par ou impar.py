
''' recursão mutua '''

def par(n):
    if n == 0:
        return True
    else:
        return impar(n-1)

def impar(n):
    if n == 0:
        return False
    else:
        return par(n-1)




#----# teste #----#

n= [0,1,2,3,4]

for valor in n:
    print('%d é par?' %valor, par (valor))
    print('%d é ímpar?' %valor, impar (valor))

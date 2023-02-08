def main():

    lista = [1,2,3,'oi']
    num_inteiro = 10
    num_real = 3.14


    print('valores antes da muda(): \n', lista, num_inteiro, num_real)
    muda(lista, num_inteiro, num_real)
    print('valores depois da muda(): \n', lista, num_inteiro, num_real)

def muda (l,ni,nr):
    l.append('tchau')
    ni *=100
    nr /= 2.5

    print('valored dentro da funcao muda (): \n', l,ni,nr)
    print()

main()

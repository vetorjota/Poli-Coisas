'''exercício da torre de Hanói

Recebe n, representando qte de discos de diametros diferentes em uma torre.

imprime qtde de passos p transferir discos do pino A para o pino B, usando o pino C como auxiliar.

discos menores sobre maiores.

'''


def hanoi(n, pino_inicio, pino_destino, pino_aux):

        if n == 1:
                print ("Mova de " , pino_inicio, "para", pino_destino)
        else:
                hanoi(n-1,pino_inicio,pino_aux,pino_destino)
                print("Mova de " ,pino_inicio, "para", pino_destino)
                hanoi(n-1,pino_aux,pino_destino,pino_inicio)
                

def main():

        num_discos = int(input("Digite o número de discos da torre de hanoi: "))
        print("A solução dessa torre é: ")
        print()
        hanoi(num_discos,"A","B","C")

main()

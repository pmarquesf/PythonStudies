n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

op = -1

while(op!=5):

    op = int(input('Digite uma opçao: '))

    if op == 1:
        print('Soma: {}'.format(n1+n2))
    elif op == 2:
        print('Multiplicacao: {}'.format(n1*n2))
    elif op == 3:
        print('Maior: ', end = ' ')
        if n1 > n2:
            print(n1)
        elif n1 < n2:
            print(n2)
        else:
            print('Iguais!')
    elif op == 4:
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    elif op == 5:
        print('Obrigado por utilizar!')
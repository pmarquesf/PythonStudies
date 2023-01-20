import random

n = -1
tentativas = 0

valor = random.randint(0,10)

while n != valor:

    n = int(input('Digite um numero (0-10): '))

    tentativas = tentativas + 1

    if n == valor:
        print('\nVocê acertou o número ({}). Parabéns!\n'.format(valor))
        print('Número de tentativas: {}'.format(tentativas))

    



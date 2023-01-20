import random

valor = random.randint(0,5)

n = int(input('Digite um numero (0-5): '))

if n == valor:
    print('Você acertou o número ({}). Parabéns!\n'.format(valor))
else:
    print('Você errou o número. A resposta era {}'.format(valor))



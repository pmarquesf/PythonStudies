import random

v = 0

while True:

    pc = random.randint(0,5)
    me = int(input('Digite um valor: '))

    if (pc + me) % 2 != 0:
        break
    
    print(f'Você ganhou! Resultado: {pc+me}')
    v += 1

print('Voce perdeu! Resultado: {}'.format(pc+me))
print('Vitórias consecutivas: {}'.format(v))
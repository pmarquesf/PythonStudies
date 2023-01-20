v = int(input('Digite a velocidade: '))

if v > 80:
    print('Você foi multado em R$ {:.2f} por excesso de velocidade!\n'.format((v-80)*7))
else:
    print('Tudo certo! Você não ultrapassou os limites de velocidade...')

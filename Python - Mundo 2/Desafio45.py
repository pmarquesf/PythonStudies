import random as r

print('1 - Pedra / 2 - Papel / 3 - Tesoura. Digite qualquer tecla para começar!')

op = int(input('Sua vez: '))
pc = r.randint(1,3)

print(op)
print(pc)

while True:
    if op == pc:
        op = str('Empate. Tente outra vez: ')
        pc = r.randint(1,3)
    if op == 1:
        if pc == 2:
            print('Você perdeu. O computador escolheu PAPEL!')
            break
        elif pc == 3:
            print('Você venceu. O computador escolheu TESOURA!')
            break
    elif op == 2:
        if pc == 1:
            print('Você venceu. O computador escolheu PEDRA!')
            break
        elif pc == 3:
            print('Você perdeu. O computador escolheu TESOURA!')
            break
    elif op == 3:
        if pc == 1:
            print('Voce perdeu. O computador escolheu PEDRA!')
            break
        elif pc == 2:
            print('Voce venceu. O computador escolheu PAPEL!')
            break
    


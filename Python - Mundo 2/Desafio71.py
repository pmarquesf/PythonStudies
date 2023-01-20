valor = int(input('Qual valor a ser sacado: '))

while True:

    if valor == 0:
        break

    if valor >= 50:
        print('{} cédulas de 50 reais!'.format(valor//50))
        valor = valor % 50
    
    if valor >= 20:
        print('{} cédulas de 20 reais!'.format(valor//20))
        valor = valor % 20

    if valor >= 10:
        print('{} cédulas de 10 reais!'.format(valor//10))
        valor = valor % 10

    if valor >= 1:
        print('{} cédulas de 1 reais!'.format(valor//1))
        valor = valor % 1 

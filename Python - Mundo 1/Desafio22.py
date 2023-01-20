nome = input('Qual seu nome completo: ')

print(nome.upper())
print(nome.lower())
print('Quantidade de letras: {}'.format(len(nome)-nome.count(' ')))

nome = nome.split()

print('Quant letras primeiro nome: {}'.format(len(nome[0])))
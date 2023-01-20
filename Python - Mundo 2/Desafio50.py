soma = 0

for i in range(1,7):
    valor = int(input('Valor {}: '.format(i)))
    if valor % 2 == 0:
        soma += valor
print(soma)
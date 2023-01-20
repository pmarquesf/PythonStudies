lista = []

while True:

    n = int(input('Digite um numero: '))

    if n in lista:
        print('Valor já existente!', end=' ')
    else:
        lista.append(n)

    op = str(input('Deseja continuar (S/N): '))

    if op == 'N':
        break

lista.sort()
print(lista)


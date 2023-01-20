lista = []
pares = []
impares = []
c = 0

while True:

    n = int(input('Digite um numero: '))

    lista.append(n)
    c += 1

    op = str(input('Deseja continuar (S/N): '))

    if op == 'N':
        break

for i in range(0, len(lista)):
    
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

lista.sort()
pares.sort()
impares.sort()

print(f'Lista Geral: {lista}')
print(f'Lista Pares: {pares}')
print(f'Lista Impares: {impares}')




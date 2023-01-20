lista = []


for i in range(0, 5):
    v = int(input(f'Valor {i+1}: '))
    lista.append(v)

print(f'Lista: {lista}')

i = 0

maior = lista[0]
menor = lista[0]

for i in lista:
    if i > maior:
        maior = i
        pmaior = lista.index(maior)
    elif i < menor:
        menor = i
        pmenor = lista.index(menor)

print(f'Menor: {menor} na posição {pmenor}')
print(f'Maior: {maior} na posição {pmaior}')

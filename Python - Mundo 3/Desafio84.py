pessoa = []
conjunto = []
qnt = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(str(input('Peso: ')))
    conjunto.append(pessoa)
    qnt += 1

    if str(input('Deseja continuar (S/N): ')) == 'N':
        break

pesadas = []
leves = []
c = 0

for i in range(0, len(conjunto)):
    if i == 0:
        pesadas.append(conjunto[i])
    
        
print(f'\nQuantidade de pessoas: {qnt}')
print(f'Pessoas mais pesadas: {pesadas}')
print(f'Pessoas mais leves: {leves}')
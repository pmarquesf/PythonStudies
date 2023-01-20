qnt = valorTotal = 0

while True:
    nome = str(input('Nome Produto: '))
    preco = float(input('Valor Produto: '))

    op = str(input('Deseja continuar (S/N): '))

    valorTotal += preco

    if preco >= 1000:
        qnt += 1

    if op == 'N':
        break 

print(f'Quantidade produtos com valor maior que R$ 1000.00: {qnt}')
print('Total gasto: R$ {:.2f}'.format(valorTotal))


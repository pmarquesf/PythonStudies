lista = []
c = 0

while True:

    n = int(input('Digite um numero: '))

    lista.append(n)
    c += 1

    op = str(input('Deseja continuar (S/N): '))

    if op == 'N':
        break

lista.sort(reverse=True)
print(f'A) {lista}')
print(f'B) {c}')

if 5 in lista:
    print(f'C) {lista.count(5)} vezes')
else:
    print('C) Não aparece!')


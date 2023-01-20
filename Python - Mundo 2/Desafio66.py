n = s = qnt = 0

while True:
    n = int(input('Digite um numero: '))

    if n == 999:
        break

    s += n
    qnt += 1

print(f'Qnt numeros: {qnt}')
print(f'Soma numeros: {s}')
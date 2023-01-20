x = 1

n = int(input('Valor: '))

for i in range(1, n+1):
    if n % i == 0:
        if i != 1 and i != n:
            x = 0
if x == 0:
    print('O numéro nao é primo!')
else:  
    print('O numero é primo!')
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(p1, p1+(razao*10), razao):
    print(i)
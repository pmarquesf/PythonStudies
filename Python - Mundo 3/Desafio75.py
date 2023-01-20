
tupla = (int(input('Valor 1: ')), int(input('Valor 2: ')), int(input('Valor 3: ')), int(input('Valor 4: ')))

print(tupla.count(9))

if 3 in tupla:  
    print(tupla.index(3))
else:
    print('Não tem 3!')

for i in tupla:
    if i % 2 == 0:
        print(i, end = ' ')
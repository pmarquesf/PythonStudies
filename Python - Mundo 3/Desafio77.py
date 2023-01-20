tupla = ('teste', 'comentario', 'celular', 'livro', 'televisao')

for i in range(0, len(tupla)):
    print('Vogais na palavra: {}'.format(tupla[i]))
    for x in range(len(tupla[i])): 
        if tupla[i][x] in 'aeiou':
            print('{}'.format(tupla[i][x]), end=' ')
    print('\n')
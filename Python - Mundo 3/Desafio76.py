tupla = ('Banana', 19.99, 'Pêra', 15.90, 'Beterraba', 12.60, 'Alho', 23.50, 'Hortelã', 9.79)

for i in range(0, len(tupla), 2):
    print('{:15} {:-5.2f}'.format(tupla[i], tupla[i+1]))

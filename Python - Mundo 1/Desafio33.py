n1 = int(input('First number: '))
n2 = int(input('Second number: '))
n3 = int(input('Third number: '))

if(n1>n2 and n1>n3):
    if(n2>n3):
        print('Maior: {}\nMedio: {}\nMenor: {}\n'.format(n1, n2, n3))
    else:
        print('Maior: {}\nMedio: {}\nMenor: {}\n'.format(n1, n3, n2))
if(n2>n1 and n2>n3):
    if(n1>n3):
        print('Maior: {}\nMedio: {}\nMenor: {}\n'.format(n2, n1, n3))
    else:
        print('Maior: {}\nMedio: {}\nMenor: {}\n'.format(n2, n3, n1))
if(n3>n1 and n3>n2):
    if(n1>n2):
        print('Maior: {}\nMedio: {}\nMenor: {}\n'.format(n3, n1, n2))
    else:
        print('Maior: {}\nMedio: {}\nMenor: {}\n'.format(n3, n2, n1))
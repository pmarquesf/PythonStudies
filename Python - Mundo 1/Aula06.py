n1 = input('Digite um valor:')

print(type(n1)) # verifica a classe de uma variavel

n2 = int(input('Digite um valor:'))
n3 = int(input('Digite um numero:'))

print(type(n2))

s = n2 + n3

# print('A soma entre', n1, 'e', n2 'vale', s)
print('A soma entre {} e {} vale {}'.format(n2, n3, s))

# tipos primitivos: int, float, bool, str

n = input('Digite algo: ')
print(n.isnumeric()) # verifica se a variavel contem um numero (int, float)


# Capitalizada = nem maiusculo nem minusculo (ou os dois) = istitle()
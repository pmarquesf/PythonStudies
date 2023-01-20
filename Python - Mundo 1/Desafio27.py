nome = input('Digite o nome completo: ')

nome = nome.split()

print('Primeiro nome: {}\nÚltimo nome: {}\n'.format(nome[0], nome[len(nome)-1]))
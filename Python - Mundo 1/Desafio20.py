from email.errors import MultipartConversionError
import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto Aluno: '))

pessoas = [ aluno1, aluno2, aluno3, aluno4]

## pessoas.sort() tambem funciona

random.shuffle(pessoas)

print('Ordem: ')
print(pessoas)



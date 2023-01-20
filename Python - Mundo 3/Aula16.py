lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') # () para tuplas, [] para listas e {} para dicionarios
print(lanche[0]) # apenas o 0
print(lanche[1:]) # de 1 até o final
print(lanche[0:3]) # de 0 até 3 excluindo o 3
print(lanche[-1]) # começa do final (nao conta indice 0)
print(lanche[-3:]) # do -3 (suco) até o final

# TUPLAS SÃO IMUTAVEIS (NÃO PODE SER ALTERADO DURANTE A EXECUCAO)

# print[1] = 'Vai dar erro'

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi demais')

for cont in range(0, len(lanche)):
    print('Eu vou comer {}'.format(lanche[cont]))
print('Comi demais')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posiçao {pos}')

print(sorted(lanche)) # printando em ordem alfab

a = (2, 5, 4)
b = (5, 7, 1, 2)
c = a + b # concatena as duas tuplas
print(c)
print(c.count(5)) # quantidade de vezes que tem na tupla
print(c.index(8)) # retorna a posicao de um valor (primeira ocorrencia)
print(c.index(5, 1)) # retorna posicao a partir da primeira posição

del(c) # apaga uma tupla inteira
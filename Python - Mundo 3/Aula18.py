# CONCEITO DAS COPIAS E LIGAÇÔES ENTRE LISTAS

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])

print(galera)

# 

galera1 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera1[2][1])
print(galera1[0][0])

for pessoa in galera1:
    print(pessoa[0])

# 

galera2 = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
    
print(galera2)
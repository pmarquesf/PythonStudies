num = [2, 3, 4, 5, 6, 7]
num2 = list(range(2, 8))

print(num)
print(num2)

num2[3] = 9
print(num2) # AS LISTAS SÃO TOTALMENTE MUTAVEIS

num.append(7) # ADICIONA O VALOR NO FINAL DA LISTA
num.sort(reverse=True) # ORDENA AO CONTRARIO
print(num)

num.insert(2, 0) # ADICIONA 0 NA POSIÇAO 2 (CHEGA OS OUTROS PRO LADO)
print(num)
num.pop(2) # EXCLUI O INDICE 2 DA LISTA
print(num)
num.remove(2) # REMOVE O PRIMEIRO 2 DA LISTA (DA ERRO SE AO HOUVER)
print(num)

print('\n\n')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end ='')
    
for c, v in enumerate(valores):
    print(f'\nna posição {c} encontrei o valor {v}!')

a = [2, 3, 4, 7]
b = a # NAO ESTA CRIANDO COPIA MAS SIM LIGANDO UMA NA OUTRA

print(a)
print(b)

b[2] = 8 # VAI ALTERAR NAS DUAS POIS ESTAO CONECTADAS

print(a)
print(b)

b = a[:] # AGORA SIM CRIA UMA COPIA

b[2] = 3 

print(a)
print(b)



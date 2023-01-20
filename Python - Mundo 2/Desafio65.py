i = maior = menor = cont = soma = 0

while i != -1:
    i = int(input('Digite um numero: '))
    cont += 1
    
    if cont == 1 and i != -1:
        maior = menor = i
    else:
        if i > maior and i != -1:
            maior = i
        if i < menor and i != -1:
            menor = i
        
        soma = soma + i
    
print(maior)
print(menor)
print(soma/(cont-1))
n = int(input('Digite um valor: '))

i = 0
lista = []
valor = 0 

while i < n:
    if i == 1 or i == 0:
        valor = valor + i
        lista.append(valor)
    else:
        valor = lista[i-1] + lista[i-2] 
        lista.append(valor)
    i+=1   
    
print(lista)

p1 = int(input('Primeiro termo: ')) 
razao = int(input('Razão: '))

i = p1 # i = 2
qnt = 10 

teste = razao*(qnt) 

while qnt != 0:

    while i < (p1+teste): 
        print(i)
        i += razao 

    qnt = int(input('Quantos numeros: '))
    teste = teste + razao*(qnt) 
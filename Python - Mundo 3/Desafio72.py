tupla = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True: 
    op = int(input('Digite um valor: '))

    if op >=0 and op <=20:
        print(tupla[op])
        break

    print('Numero invalido. ', end=' ')
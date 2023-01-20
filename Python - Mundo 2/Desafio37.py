import math

texto = '\n  - Decimal p/ Binario\n  - Decimal p/ Octal\n  - Decimal p/ Hexadecimal\n\nDigite a base que deseja converter: '

n = int(input('\nDigite um numero para converter: '))
op = int(input(texto))

resultado = []
i=0
t = n

def verificarResto(y, i):
    if y == 10:
        resultado.insert(i, 'A')
    elif y == 11:
        resultado.insert(i, 'B')
    elif y == 12:
        resultado.insert(i, 'C')
    elif y == 13:
        resultado.insert(i, 'D')
    elif y == 14:
        resultado.insert(i, 'E')
    elif y == 15:
        resultado.insert(i, 'F')
    elif y == 16:
        resultado.insert(i, 'G')

def verificarN(y):
    if y == 10:
        resultado.insert(0, 'A')
    elif y == 11:
        resultado.insert(0, 'B')
    elif y == 12:
        resultado.insert(0, 'C')
    elif y == 13:
        resultado.insert(0, 'D')
    elif y == 14:
        resultado.insert(0, 'E')
    elif y == 15:
        resultado.insert(0, 'F')
    elif y == 16:
        resultado.insert(0, 'G')

if op==1:
    if n==1:
        print(1)
    else:
        while n>=2:
            aux = n  
            n = n // 2 
            resto = aux % 2 
            resultado.insert(i, str(math.floor(resto)))  # FUNCAO INSERT TEVE QUE SER UTILIAZDA POIS O INDICE NAO PODE SER ATRIBUIDO EM PYTHON COMO ERA EM C
            i=i+1
        resultado = resultado[::-1]
        resultado.insert(0, str(n))
        r = ''.join(resultado) # RETIRA OS COLCHETES E VIRGULAS
        print('{} (dec) -> {} (bin)'.format(t, r))
elif op==2:
    if n==1:
        print(1)
    else:
        while n>=8:
            aux = n  
            n = n // 8 
            resto = aux % 8 
            resultado.insert(i, str(math.floor(resto)))
            i=i+1
        resultado = resultado[::-1]
        resultado.insert(0, str(n))
        r = ''.join(resultado)
        print('{} (dec) -> {} (oct)'.format(t, r))
elif op==3:
    if n==1:
        print(1)
    else:
        while n>=16:
            aux = n  
            n = n // 16 
            resto = aux % 16 

            if resto < 10:
                resultado.insert(i, str(math.floor(resto)))
            else:
                verificarResto(resto, i)
            i=i+1
        resultado = resultado[::-1]
        if resto < 10:
                resultado.insert(0, str(n))
        else:
            verificarN(n)
        r = ''.join(resultado)          
        print('{} (dec) -> {} (hex)'.format(t, r))
else:
    print('Opção inválida!\n')



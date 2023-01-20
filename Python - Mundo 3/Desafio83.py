exp = str(input('Digite uma expressão: '))
p = 0

for i in range(0, len(exp)):
    if exp[i] == '(':
        p += 1
    elif exp[i] == ')':
        if p == 0:
            print('Expressão está errada!')
        else:
            p -= 1
    if i == len(exp)-1:
        if  p == 0:
            print ('Sua expressão está correta!')
        else:
            print('Expressão está errada!')

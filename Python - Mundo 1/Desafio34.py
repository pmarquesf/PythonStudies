salario = float(input('Qual seu salario: '))

if salario > 1250:
    print('Novo Salario: {:.2f}\n'.format(salario + (salario*0.10)))
else:
    print('Novo Salario: {:.2f}\n'.format(salario + (salario*0.15)))
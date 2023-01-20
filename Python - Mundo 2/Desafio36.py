valor = float(input('Qual o valor da casa: '))
salario = float(input('Qual seu salario: '))
anos = int(input('Quantos anos você vai levar para pagar: '))

prestacao = valor / (anos*12)

if prestacao <= (salario * 0.3):
    print('As parcelas serão de R$ {:.2f}\n'.format(prestacao))
else:
    print('Infelizmente o empréstimo foi negado\n')
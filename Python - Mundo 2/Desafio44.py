valor = float(input('Valor do produto: R$ '))
op = int(input('Forma de pagamento (1 - Dinheiro/Cheque à vista // 2 - Cartão à prazo / à vista): '))

if op == 1:
    print('Valor total: {:.2f}'.format(valor-(valor*0.1)))
elif op == 2:
    op2 = int(input('Em quantas parcelas você quer pagar no cartão: '))
    if op2 == 1:
        print('Valor total: {:.2f}'.format(valor - (valor*0.05)))
    elif op2 == 2:
        print('Valor total: {:.2f}'.format(valor))
    else:
        print('Valor total: {:.2f}'.format(valor + (valor*0.2)))


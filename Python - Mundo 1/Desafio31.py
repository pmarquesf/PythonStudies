distancia = int(input('Digite a distancia da viagem: '))

if distancia > 200:
    print('Valor da passagem: R$ {:.2f}'.format(0.45*distancia))
else:
    print('Valor da passagem: R$ {:.2f}'.format(0.50*distancia))

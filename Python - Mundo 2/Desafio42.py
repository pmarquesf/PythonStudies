peso = float(input('Qual seu peso (KG): '))
altura = float(input('Qual sua altura (m): '))

imc = peso / pow(altura, 2)

print('Seu IMC: {:.2f}'.format(imc))

if imc < 18.5:
    print('\nClassificação: Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('\nClassificação: Peso ideal')
elif imc >= 25 and imc < 30:
    print('\nClassificação: Sobrepeso')
elif imc >= 30 and imc < 40:
    print('\nClassificação: Obesidade')
else:
    print('\nObesidade Mórbida')
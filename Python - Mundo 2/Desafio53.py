text = input('Qual a frase: ')

# Método com IF

text = text.replace(" ", "").lower()
textInvert = text[::-1]

if text == textInvert:
    print('É um palindromo')
else:
    print('Não é um palindromo')



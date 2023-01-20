frase = input('Digite uma frase: ')

print('Quantidad de "A": ', frase.count('a'))

print('Primeiro "a": ', frase.find('a'))

frase2 = frase[::-1]

print('Ultimo "a": ', len(frase) - frase2.find('a'))

# PODERIA UTILIZAR A FUNCAO RFIND (PROCURA A PARTIR DO LADO DIREITO)





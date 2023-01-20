qntH = idadeM = maiores = 0

while True:
    sexo = str(input('Sexo (M/F): '))
    idade = int(input('Idade: '))

    op = str(input('Deseja continuar (S/N): '))

    if sexo=='M':
        qntH += 1

    if sexo=='F' and idade <20:
        idadeM += 1

    if idade >= 18:
        maiores += 1

    if op == 'N':
        break

print(idadeM)
print(qntH)
print(maiores)


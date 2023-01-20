soma = 0
mulheres = 0

for i in range(1,5):
    nome = input('Nome {}° Pessoa: '.format(i))
    idade = int(input('Idade {}° Pessoa: '.format(i)))
    sexo = input('Sexo {}° Pessoa (M/F): '.format(i))

    soma += idade

    if i == 1:
        maisvelho = idade

    if sexo == 'F' and idade < 20:
        mulheres += 1

    if sexo == 'M' and idade > maisvelho:
        homem = nome

print('\n')
print('Media das idades: {:.2f}'.format(soma/4))
print('Homem mais velho: {}'.format(homem))
print('Qnt mulheres < 20 anos: {}'.format(mulheres))

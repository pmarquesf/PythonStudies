from smtpd import MailmanProxy


for i in range(1, 7):
    peso = float(input('Peso {}: '.format(i)))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Maior: {:.2f}'.format(maior))
print('Menor: {:.2f}'.format(menor))

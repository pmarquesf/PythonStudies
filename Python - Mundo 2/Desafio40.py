import datetime as dt

ano = int(input('Qual seu ano de nascimento: '))

today = str(dt.date.today())
today = today.split('-')[::-1]

idade = int(today[2]) - ano

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <=19:
    print('Júnior')
elif idade <=25:
    print('Sênior')
else: 
    print('Master')


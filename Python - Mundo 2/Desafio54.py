import datetime as dt

maiores = 1

today = str(dt.date.today())
today = today.split('-')[::-1]

for i in range(1, 9):
    print('Pessoa 1: ')
    dia = int(input('Dia: '))
    mes = int(input('Mes: '))
    ano = int(input('Ano: '))

    if int(today[2])-ano >= 18:
        maiores += 1

print(maiores)









import datetime as dt

dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))

today = str(dt.date.today())

today = today.split('-')[::-1]

print(today)

if int(today[2])-ano == 18:
    print('Você está no momento exato do alistamento!')
elif int(today[2])-ano < 18:
    print('Você ainda não está na idade do alistamento!')
else:
    print('Voce perdeu o prazo do alistamento militar!')









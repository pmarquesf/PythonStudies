while True:

    n = int(input('Digite um valor: '))

    if n < 0:
        break

    for i in range(1,11):
        print('{} x {} = {}'.format(i, n, n*i))

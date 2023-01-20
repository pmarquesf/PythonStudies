l1 = int(input('First side: '))
l2 = int(input('Second side: '))
l3 = int(input('Third side: '))

if((l2-l3) < l1 < (l2+l3) or ( l1 - l3 ) < l2 < (l1 + l3) or ( l1 - l2 ) < l3 < (l1 + l2)):
    print('Voce PODE formar um triangulo!')
else:
    print('Voce NAO pode formar um triangulo')

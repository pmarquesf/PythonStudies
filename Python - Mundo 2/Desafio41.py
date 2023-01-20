l1 = int(input('First side: '))
l2 = int(input('Second side: '))
l3 = int(input('Third side: '))

if((l2-l3) < l1 < (l2+l3) or ( l1 - l3 ) < l2 < (l1 + l3) or ( l1 - l2 ) < l3 < (l1 + l2)):
    if l1==l2 and l1==l3:
        print('Voce PODE formar um triangulo do tipo EQUILATERO')
    elif l1!=l2 and l1!=3 and l2!=l3:
        print('Voce PODE formar um triangulo do tipo ESCALENO')
    else:
        print('Voce PODE formar um triangulo do tipo ISOSCELES')
else:
        print('Voce NAO pode formar um triangulo')

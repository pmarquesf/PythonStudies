import math

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjascente: '))

hip = math.hypot(co, ca)

print('Hipotenusa: {}'.format(hip))
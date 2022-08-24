# Catetos e hipotenusa

from math import sqrt, pow, hypot

cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))

hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))

hi = hypot(cateto_oposto, cateto_adjacente)

print(hi)

print('O comprimento da hipotenusa é {:.1f}.'.format(hipotenusa))

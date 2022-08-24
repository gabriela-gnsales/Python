# Quebrando um número

from math import trunc

n = float(input('Digite um número: '))

print('O número {:.4f} tem a parte inteira igual a {}.'.format(n, trunc(n)))

print('Outra maneira usando int: ', int(n))

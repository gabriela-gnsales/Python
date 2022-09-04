# Cálculo do fatorial

from math import factorial

n = int(input('Quer saber o fatorial de qual número? '))

# --------------- #

f = factorial(n)
print(f'O fatorial de {n} é {f}.')

# --------------- #

fatorial_for = 1
for i in range(n, 1, -1):
    fatorial_for *= i

print(f'Fatorial FOR: {n}! = {fatorial_for}')

# --------------- #

fatorial_while = 1
c = n
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial_while *= c
    c -= 1
print(fatorial_while)

print(f'\nFatorial WHILE: {n}! = {fatorial_while}')

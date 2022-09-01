# Números primos

n = int(input('Informe um nº: '))

c = 0
for i in range(1, n+1):
    if n % i == 0:
        c += 1
        print(f'{n} % {i} = {n % i}')

if c == 2:
    print(f'\033[1;36m{n} é um número PRIMO!\033[m')
else:
    print(f'\033[1;31m{n} NÃO é um número primo!\033[m')

for i in range(1, n+1):
    if n % i == 0:
        print('\033[1;33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end=' ')

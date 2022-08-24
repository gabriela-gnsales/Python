# Tabuada

n = int(input('Digite o nº que você quer saber a tabuada: '))

print(11 * '-')

for i in range(1, 11):
    print('{} x {:<2} = {:<2}'.format(n, i, n*i))

print(11 * '-')
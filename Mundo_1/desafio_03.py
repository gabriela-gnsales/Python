# Somando dois números

n1 = int(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))

print('Tipo do 1º número: {}'.format(type(n1)))
print('Tipo do 2º número: {}'.format(type(n2)))

print('A soma dos dois números é', n1 + n2)

s = n1 + n2
print('Tipo da variável s: {}'.format(type(s)))

print('A soma de {} e {} vale {}!'.format(n1, n2, s))

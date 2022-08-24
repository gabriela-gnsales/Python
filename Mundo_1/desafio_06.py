# Dobro, triplo e raíz quadrada

n = int(input('Digite um nº: '))

d = n * 2
t = n * 3
r = n ** (1/2)  # pow(n, (1/2))

print('O dobro do nº é {}, o triplo é {} e a raiz quadrada é igual a {:.4f}.'.format(d, t, r))

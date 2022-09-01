# Soma ímpares múltiplos de 3

soma = cont = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        # print(i)
        soma += i
        cont += 1

print(f'Iterações = {i}')
print(f'Soma = {soma}')
print(f'A soma de todos os {cont} valores solicitados é {soma}.')

s = c = j = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        # print(n)
        s += n
        c += 1
    j += 1

print(f'Iterações = {j}')
print(f'Soma = {s}')
print(f'A soma de todos os {c} valores solicitados é {s}.')

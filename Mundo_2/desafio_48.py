# Soma ímpares múltiplos de 3

soma = 0
for i in range(1, 500+1):
    if i % 2 != 0 and i % 3 == 0:
        print(i)
        soma += i

print(f'Soma = {soma}')

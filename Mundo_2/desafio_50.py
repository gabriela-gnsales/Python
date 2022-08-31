# Soma dos pares

soma = 0
for i in range(1, 7):
    n = int(input(f'{i}º número: '))
    if n % 2 == 0:
        # print(n)
        soma += n
        # print('Soma = ', soma)

print('Soma dos números pares = ', soma)

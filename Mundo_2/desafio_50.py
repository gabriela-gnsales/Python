# Soma dos pares

soma = c = 0
for i in range(1, 7):
    n = int(input(f'{i}º número: '))
    if n % 2 == 0:
        # print(n)
        soma += n
        # print('Soma = ', soma)
        c += 1

print(f'Você informou {c} números PARES e a SOMA deles é {soma}.')

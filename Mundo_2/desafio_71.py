# Simulador de caixa eletrônico

print('=' * 40)
print('{:^40}'.format('CAIXA ELETRÔNICO'))
print('=' * 40)

valor = int(input('Qual valor você quer sacar? R$ '))

# cédulas: R$ 50, R$ 20, R$ 10 e R$ 1
'''
n_50 = n_20 = n_10 = n_1 = 0

if valor // 50 > 0:
    n_50 = valor // 50
    valor -= 50 * n_50
if valor // 20 > 0:
    n_20 = valor // 20
    valor -= 20 * n_20
if valor // 10 > 0:
    n_10 = valor // 10
    valor -= 10 * n_10
if valor < 10:
    n_1 = valor

if n_50 == 1:
    print(f'Total de {n_50} cédula de R$ 50.')
elif n_50 > 1:
    print(f'Total de {n_50} cédulas de R$ 50.')

if n_20 == 1:
    print(f'Total de {n_20} cédula de R$ 20.')
if n_20 > 1:
    print(f'Total de {n_20} cédulas de R$ 20.')

if n_10 == 1:
    print(f'Total de {n_10} cédula de R$ 10.')
if n_10 > 1:
    print(f'Total de {n_10} cédulas de R$ 10.')

if n_1 == 1:
    print(f'Total de {n_1} cédula de R$ 1.')
if n_1 > 1:
    print(f'Total de {n_1} cédulas de R$ 1.')

print('=' * 40)

'''
# OUTRO MODO

total = valor
ced = 50
tot_ced = 0
while True:
    if total >= ced:
        total -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} cédulas de R$ {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0
        if total == 0:
            break

print('=' * 40)

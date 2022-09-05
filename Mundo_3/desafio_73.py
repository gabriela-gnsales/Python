# Tuplas com times de futebol

brasileirao_2022 = ('Palmeiras', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Internacional', 'Athletico-PR', 'Athletico-MG', 'América-MG', 'Santos')

print(len(brasileirao_2022))

print('Brasileirão 2022 (10 primeiros colocados):', brasileirao_2022)

for time in brasileirao_2022:
    print(f'{time} -> ', end='')
print('FIM')

for pos, time in enumerate(brasileirao_2022):
    print(f'{(pos+1):2}º: {time}')

print('Primeiros 5 colocados:', brasileirao_2022[:5])

print('Primeiros 5 colocados: ', end='')
for j in range(5):
    print(f'{j+1}º: {brasileirao_2022[j]}', end=' | ')

print('\nÚltimos 4 colocados:', brasileirao_2022[-4:])

print('Últimos 4 colocados: ', end='')
for j in range(-4, 0):
    print(f'{j+11}º: {brasileirao_2022[j]}', end=' | ')

print('\nTimes em ordem alfabética:', sorted(brasileirao_2022))

print(f'Posição do time Athletico-PR na tabela do Brasileirão de 2022: {brasileirao_2022.index("Athletico-PR") + 1}º lugar.')

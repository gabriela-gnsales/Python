# Lista composta e análise de dados

print('=' * 40)

temporaria = list()
principal = list()
maior = menor = 0
while True:
    temporaria.append(input('Nome: ').strip().capitalize())
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()

    r = input('Deseja continuar cadastrando [S/N]: ').strip().upper()[0]
    while r not in 'SN':
        print('Opção inválida! Responda novamente:')
        r = input('Deseja continuar cadastrando [S/N]: ').strip().upper()[0]
    if 'N' in r:  # if r in 'N':
        break

print('=' * 40)

print('Lista completa:', principal)

print(f'Foram cadastradas {len(principal)} pessoas.')

print(f'O maior peso foi {maior} kg e o menor foi {menor} kg.')

print(f'O maior peso foi {maior} kg de', end=' ')
for pos in range(len(principal)):
    if principal[pos][1] == maior:
        print(f'{principal[pos][0]}...', end=' ')

print(f'\nO menor peso foi {menor} kg de', end=' ')
for pos in range(len(principal)):
    if principal[pos][1] == menor:
        print(f'{principal[pos][0]}...', end=' ')

print(f'\nO maior peso foi {maior} kg de', end=' ')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi {menor} kg de', end=' ')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')

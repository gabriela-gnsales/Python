# Maior e menor valores na lista

numeros = list()
for n in range(1, 6):
    num = int(input(f'{n}º valor: '))
    numeros.append(num)
print('Lista:', numeros)

# print(numeros[0])
# print(numeros[1])

menor = min(numeros)
maior = max(numeros)
print(f'O menor valor da lista é {menor} e está na {numeros.index(menor)+1}ª posição.')
print(f'O maior valor da lista é {maior} e está na {numeros.index(maior)+1}ª posição.')

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i+1}ª...', end=' ')

print(f'\nO maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i+1}ª...', end=' ')

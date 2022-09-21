# Dividindo valores em várias listas

print('=-' * 30)

lista = list()
while True:
    v = int(input('Insira um valor na lista [para sair digite 0]: '))
    if v == 0:
        break
    lista.append(v)

lista_pares = list()
lista_impares = list()
for v in lista:
    if v % 2 == 0:
        lista_pares.append(v)
    else:
        lista_impares.append(v)

print('=-' * 30)

print(f'Lista completa com {len(lista)} números: {lista}')
print(f'Lista de pares com {len(lista_pares)} números: {lista_pares}')
print(f'Lista de ímpares com {len(lista_impares)} números: {lista_impares}')

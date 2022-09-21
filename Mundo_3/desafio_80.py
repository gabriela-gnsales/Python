# Lista ordenada sem repetições

print('=-' * 30)

lista = []

for c in range(1, 6):
    valor = int(input(f'Digite o {c}º valor: '))
    if c == 1:
        lista.append(valor)
    elif valor < lista[0]:
        lista.insert(0, valor)
        print(f'Número {valor} adicionado na primeira posição da lista.')
    elif valor > lista[-1]:
        lista.append(valor)
        print(f'Número {valor} adicionado na última posição da lista.')
    else:
        # pos = 0
        # while pos < len(lista):
        #     if valor <= lista[pos]:
        #         lista.insert(pos, valor)
        #         print(f'Número {valor} adicionado na {pos+1}ª posição da lista.')
        #         break
        #     pos += 1
        for pos, n in enumerate(lista):
            if valor <= n:
                lista.insert(pos, valor)
                break
        print(f'Número {valor} adicionado na {pos+1}ª posição da lista.')

print('=-' * 30)
print('Os valores digitados em ordem foram:', lista)

# Extraindo dados de uma lista

print('=-' * 30)

lista = list()
while True:
    v = int(input('Insira um valor na lista [para sair digite 0]: '))
    if v == 0:
        break
    lista.append(v)

print('=-' * 30)

print('Lista:', lista)
print('Lista ordenada:', sorted(lista))
print(f'A lista possui {len(lista)} números.')

lista_decrescente = lista[:]
lista_decrescente.sort(reverse=True)
print('Lista ordenada de forma decrescente:', lista_decrescente)

if 5 in lista:
    print(f'O número 5 foi digitado e está na {lista.index(5)+1}ª posição da lista original e na {lista_decrescente.index(5)+1}ª posição da lista ordenada de forma decrescente.')
else:
    print('O número 5 não foi digitado.')

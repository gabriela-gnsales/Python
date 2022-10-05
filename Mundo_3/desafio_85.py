# Listas com pares e ímpares

print('=' * 40)
'''
total = []
pares = []
impares = []
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
total.append(pares)
total.append(impares)
print('Lista completa:', total)
print('Valores pares:', sorted(pares))  # desse jeito não muda a lista original dos pares, só mostra ordenado nesse print
impares.sort()  # desse jeito altera a lista original dos ímpares
print('Valores ímpares:', impares)
'''
# OUTRO MODO
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=' * 40)
print('Todos os valores:', num)
# num[0].sort()
# num[1].sort()
print('Valores pares:', sorted(num[0]))
print('Valores ímpares:', sorted(num[1]))



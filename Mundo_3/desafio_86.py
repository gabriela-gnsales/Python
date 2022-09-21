# Matriz em python

print('=' * 40)
'''
matriz_temp = []
matriz_princ = []
n = 0
for i in range(1, 4):
    for j in range(1, 4):
        matriz_temp.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    matriz_princ.append(matriz_temp[:])
    matriz_temp.clear()
    
print('=' * 40)
print(matriz_princ)

for pos, n in enumerate(matriz_princ):
    j = 0
    for i in range(1, 4):
        if pos == j:
            # print(f'[{matriz_princ[pos][i]}]', end=' ')
            print(f'[{n}]', end=' ')
        else:
            print('')
    j += 1
'''
# OUTRO MODO

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1}, {c+1}]: '))

print('=' * 40)
print(matriz)

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()

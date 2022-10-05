# Mais sobre matriz em python

matriz_principal = []
matriz_temporaria = []

num_l = int(input('Número de linhas da matriz: '))
num_c = int(input('Número de colunas da matriz: '))

soma_par = 0
for l in range(num_l):
    for c in range(num_c):
        num = int(input(f'Digite um valor para [{l+1}, {c+1}]: '))
        matriz_temporaria.append(num)
        if num % 2 == 0:
            soma_par += num
    matriz_principal.append(matriz_temporaria[:])
    matriz_temporaria.clear()

print('=' * 40)

soma_ultima_coluna = maior_primeira_linha = 0
for l in range(num_l):
    for c in range(num_c):
        print(f'[{matriz_principal[l][c]:^5}]', end=' ')
        if c+1 == num_c:
            soma_ultima_coluna += matriz_principal[l][c]
        if l == 0:
            if matriz_principal[l][c] > maior_primeira_linha:
                maior_primeira_linha = matriz_principal[l][c]
    print()

print('=' * 40)

print(f'A soma dos valores pares é {soma_par}.')
print(f'A soma dos valores da última coluna é {soma_ultima_coluna}.')
print(f'O maior valor da primeira linha é {maior_primeira_linha}.')

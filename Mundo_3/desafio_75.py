# Análise de dados em uma tupla

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))
n4 = int(input('Digite um número inteiro: '))

num = (n1, n2, n3, n4)

print('Número de vezes que apareceu o valor 9:', num.count(9))

# if 9 in num:
#     print('Número de vezes que apareceu o valor 9:', num.count(9))
# else:
#     print('Não foi digitado o número 9.')

if 3 in num:
    print(f'Posição do primeiro valor 3: {num.index(3) + 1}ª')
else:
    print('Não foi digitado o número 3.')

print('Números pares: ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' - ')

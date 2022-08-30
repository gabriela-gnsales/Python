# Conversor de bases numéricas

n = int(input('Informe um nº inteiro: '))
base_conversao = int(input('''Informe a base de conversão que deseja:
\033[1;31m*\033[m \033[1;36m1\033[m para binário
\033[1;31m*\033[m \033[1;36m2\033[m para octal
\033[1;31m*\033[m \033[1;36m3\033[m para hexadecimal 
'''))

print(base_conversao)

# while base_conversao != 1 or base_conversao != 2 or base_conversao != 3:
while not base_conversao == 1 or not base_conversao == 2 or not base_conversao == 3:
    print('Opção inválida!')
    base_conversao = int(input('Informe novamente a base de conversão que deseja (1, 2 ou 3): '))

if base_conversao == 1:
    print(f'O número {n} no sistema binário é x.')
elif base_conversao == 2:
    print(f'O número {n} no sistema octal é y.')
else:
    print(f'O número {n} no sistema hexadecimal é z.')

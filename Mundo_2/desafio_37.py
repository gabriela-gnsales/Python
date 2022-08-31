# Conversor de bases numéricas

n = int(input('Informe um nº inteiro: '))
base_conversao = int(input('''Escolha uma das bases para conversão:
\033[1;31m[\033[m \033[1;36m1\033[m \033[1;31m]\033[m converter para BINÁRIO
\033[1;31m[\033[m \033[1;36m2\033[m \033[1;31m]\033[m converter para OCTAL
\033[1;31m[\033[m \033[1;36m3\033[m \033[1;31m]\033[m converter para HEXADECIMAL
Sua opção: '''))

# print(base_conversao)

# while base_conversao != 1 or base_conversao != 2 or base_conversao != 3:
# while not base_conversao == 1 or not base_conversao == 2 or not base_conversao == 3:
#     print('Opção inválida!')
#     base_conversao = int(input('Informe novamente a base de conversão que deseja (1, 2 ou 3): '))

if base_conversao == 1:
    print(f'O número \033[1;36m{n}\033[m no sistema binário é \033[1;36m{bin(n)[2:]}\033[m.')
elif base_conversao == 2:
    print(f'O número \033[1;36m{n}\033[m no sistema octal é \033[1;36m{oct(n)[2:]}\033[m.')
elif base_conversao == 3:
    print(f'O número \033[1;36m{n}\033[m no sistema hexadecimal é \033[1;36m{hex(n)[2:]}\033[m.')
else:
    print('Opção inválida. Tente novamente.')

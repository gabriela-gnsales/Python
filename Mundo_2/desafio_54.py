# Grupo da maioridade

from datetime import date

tot_maior = 0
tot_menor = 0
for i in range(1, 8):
    ano_nascimento = int(input(f'Ano de nascimento da {i}ª pessoa: '))
    idade = date.today().year - ano_nascimento
    print('Idade:', idade)
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1

print(f'\033[1;36m{tot_maior}\033[m pessoas já atingiram a maioridade e \033[1;36m{tot_menor}\033[m pessoas ainda possuem menos de 18 anos.')

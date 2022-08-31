# Grupo da maioridade

from datetime import date

maior_idade = 0
menor_idade = 0
for i in range(1, 8):
    ano_nascimento = int(input(f'Ano de nascimento da {i}ª pessoa: '))
    idade = date.today().year - ano_nascimento
    print('Idade:', idade)
    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'\033[1;36m{maior_idade}\033[m pessoas já atingiram a maioridade e \033[1;36m{menor_idade}\033[m pessoas ainda possuem menos de 18 anos.')

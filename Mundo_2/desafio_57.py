# Validação de dados

nome = input('Nome: ').strip().capitalize()
genero = input('Gênero (M/F): ').strip().lower()[0]  # pega só a primeira letra, caso o usuário digite uma palavra
# print(genero)

# OUTRO MODO
sexo = input('Sexo (M/F): ').strip()[0]

while genero != 'm' and genero != 'f':
    print('Opção inválida!')
    genero = input('Gênero (M/F): ').strip().lower()[0]

while sexo not in 'MmFf':
    print('Opção inválida!')
    sexo = input('Sexo (M/F): ').strip()[0]

print(f'Sexo {sexo.upper()} registrado com sucesso!')

if genero == 'm':
    print(f'Bem-vindo, {nome}!')
else:
    print(f'Bem-vinda, {nome}!')

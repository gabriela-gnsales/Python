# Validação de dados

nome = input('Nome: ').strip().capitalize()

genero = input('Gênero (M/F): ').strip().lower()

while genero != 'm' and genero != 'f':
    print('Opção inválida!')
    genero = input('Gênero (M/F): ').strip().lower()

if genero == 'm':
    print(f'Bem-vindo, {nome}!')
else:
    print(f'Bem-vinda, {nome}!')

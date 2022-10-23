# Unindo dicionários e listas

import titulos

titulos.titulo2('*', 50, ' CADASTRO ')

cadastro = []
tot = 0
while True:
    nome = input('Nome: ').strip().capitalize()
    while True:
        genero = input('Gênero [M/F]: ').strip().upper()[0]
        if genero in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    idade = int(input('Idade: '))
    pessoa = {
        'Nome': nome,
        'Gênero': genero,
        'Idade': idade
    }
    # pessoa = {
    #     'Nome': input('Nome: ').strip().capitalize(),
    #     'Gênero': input('Gênero [M/F]: ').strip().upper()[0],
    #     'Idade': int(input('Idade: '))
    #  }
    # cadastro.append(pessoa.copy())
    cadastro.append(pessoa)
    while True:
        resp = input('Deseja continuar cadastrando [S/N]? ').strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break

titulos.titulo2('*', 50, ' DADOS ')

soma_idade = 0
mulheres = []
print('-' * 15)
for pessoa in cadastro:
    for k, v in pessoa.items():
        if k == 'Nome':
            print(v.upper())
        else:
            print(f'{k} = {v}')
        if k == 'Idade':
            soma_idade += v
        if k == 'Gênero':
            if v == 'F':
                mulheres.append(pessoa['Nome'])
    print('-' * 15)

if len(cadastro) == 1:
    print(f'Foi cadastrada apenas 1 pessoa.')
else:
    print(f'Foram cadastradas {len(cadastro)} pessoas.')

media = soma_idade/len(cadastro)
if len(cadastro) > 1:
    print(f'A média de idade do grupo é {media:.1f} anos.')

if len(mulheres) > 0:
    print('Lista com todas as mulheres:', end=' ')
    for mulher in mulheres:
        if mulher == mulheres[-1]:
            print(mulher, end='.')
        elif mulher == mulheres[-2]:
            print(mulher, end=' e ')
        else:
            print(mulher, end=', ')

idade_acima_media = []
for pessoa in cadastro:
    for k, v in pessoa.items():
        if k == 'Idade':
            if v > media:
                idade_acima_media.append(pessoa['Nome'])

if len(idade_acima_media) > 0:
    print('\nLista de pessoas com idade acima da média do grupo:', end=' ')
    for pessoa in idade_acima_media:
        if pessoa == idade_acima_media[-1]:
            print(pessoa, end='.')
        elif pessoa == idade_acima_media[-2]:
            print(pessoa, end=' e ')
        else:
            print(pessoa, end=', ')

# Analisador completo

n_pessoas = 4
soma_idade = 0
idade_maior = 0
num_mulher = 0
homem_mais_velho = 'nome'

for i in range(1, n_pessoas+1):
    print('\33[0;33m-=\33[m'*20)
    nome = input(f'Nome da {i}ª pessoa: ').strip().lower()
    # print(nome)
    idade = int(input(f'Idade da {i}ª pessoa: '))
    sexo = input(f'Sexo da {i}ª pessoa (M ou F): ').strip().lower()
    # print(sexo)
    # print(len(sexo))

    while sexo != 'm' or sexo != 'f':
        print('Opção inválida!')
        sexo = input(f'Informe novamente o sexo da {i}ª pessoa (M ou F): ').strip().lower()
        if sexo == 'm' or sexo == 'f':
            break

    soma_idade += idade

    if sexo == 'm':
        if idade > idade_maior:
            idade_maior = idade
            homem_mais_velho = nome

    if sexo == 'f':
        if idade < 20:
            num_mulher += 1

media_idade = soma_idade / n_pessoas

print('\33[0;36m-=\33[m'*20)

print(f'A média de idade do grupo é {media_idade:.01f} anos.')

if homem_mais_velho == 'nome':
    print('Não foi registrada nenhuma pessoa do sexo masculino.')
else:
    print(f'O homem mais velho do grupo é o {(homem_mais_velho).capitalize()}.')

if num_mulher == 0:
    print('Não foi registrada nenhuma pessoa do sexo feminino com idade inferior a 20 anos.')
elif num_mulher == 1:
    print(f'{num_mulher} mulher tem menos de 20 anos.')
else:
    print(f'{num_mulher} mulheres têm menos de 20 anos.')

print('\33[0;36m-=\33[m'*20)

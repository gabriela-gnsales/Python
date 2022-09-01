# Analisador completo

n_pessoas = 2
soma_idade = idade_maior = num_mulher = 0
homem_mais_velho = ''

for i in range(1, n_pessoas+1):
    # print('\33[0;33m-=\33[m'*5, f'{i}ª PESSOA', '\33[0;33m-=\33[m'*5)
    print('\33[0;33m-=' * 5, f'{i}ª PESSOA', '-=\33[0;33m' * 5)
    nome = input('\33[mNome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()

    while sexo != 'm' and sexo != 'f':
        print('\33[1;31mOpção inválida!\33[m')
        sexo = input('Sexo [M/F]: ').strip().lower()
        # sexo = input(f'Informe novamente o sexo da {i}ª pessoa (M ou F): ').strip().lower()

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

if homem_mais_velho == '':
    print('Não foi registrada nenhuma pessoa do sexo masculino.')
else:
    print(f'O homem mais velho do grupo é o {homem_mais_velho}.')
if num_mulher == 0:
    print('Não foi registrada nenhuma pessoa do sexo feminino com idade inferior a 20 anos.')
elif num_mulher == 1:
    print(f'{num_mulher} mulher tem menos de 20 anos.')
else:
    print(f'{num_mulher} mulheres têm menos de 20 anos.')

print('\33[0;36m-=\33[m'*20)

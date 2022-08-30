# Alistamento militar

from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))

idade = date.today().year - ano_nascimento

# data_nascimento = input('Data de nascimento (dd mm aaaa): ').strip()
# data_nascimento_dividido = data_nascimento.split()
# print(data_nascimento_dividido)
# data_nascimento2 = date(year=data_nascimento_dividido[2], month=data_nascimento_dividido[1], day=data_nascimento_dividido[0])
# print('Data 2:', data_nascimento2)
# idade2 = date.today().today() - (1994, 12, 20)
# print('Data:', date.today().today())
# print('Idade:', idade2)

if idade < 18:
    if 18 - idade == 1:
        print(f'Você ainda irá se alistar ao exército daqui 1 ano.')
    else:
        print(f'Você ainda irá se alistar ao exército daqui {18 - idade} anos.')
elif idade == 18:
    print('Já está na hora de você se alistar, pois já completou 18 anos.')
else:
    if idade - 18 == 1:
        print(f'Já passou do tempo do seu alistamento há 1 ano.')
    else:
        print(f'Já passou do tempo do seu alistamento há exatos {idade - 18} anos.')

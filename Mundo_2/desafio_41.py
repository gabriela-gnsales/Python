# Classificando atletas

from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))

idade = date.today().year - ano_nascimento

print(f'Você está com {idade} anos.')

if idade <= 9:
    print('Categoria MIRIM.')
elif idade <= 14:
    print('Categoria INFANTIL.')
elif idade <= 19:
    print('Categoria JÚNIOR.')
elif idade <= 20:
    print('Categoria SÊNIOR.')
else:
    print('Categoria MASTER.')

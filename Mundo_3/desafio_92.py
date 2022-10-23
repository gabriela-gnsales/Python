# Cadastro de trabalhador

from datetime import date
import titulos


def calcula_idade(data_de_nascimento):
    data_hoje = date.today()
    idade = data_hoje.year - data_de_nascimento.year - ((data_hoje.month, data_hoje.day) < (data_de_nascimento.month, data_de_nascimento.day))
    return idade
# Teste função calcula_idade
# print(calcula_idade(date(1994, 12, 20)), 'anos')


titulos.titulo2('*', 50, ' CADASTRO ')

pessoa = dict()

pessoa['Nome'] = input('Nome: ').strip().capitalize()
data_de_nascimento = input('Data de nascimento [dd/mm/aaaa]: ').split('/')
pessoa['Idade'] = calcula_idade(date(int(data_de_nascimento[2]), int(data_de_nascimento[1]), int(data_de_nascimento[0])))
pessoa['Carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): '))

# nome = input('Nome: ').strip().capitalize()
# data_de_nascimento = input('Data de nascimento [dd/mm/aaaa]: ').split('/')
# idade = calcula_idade(date(int(data_de_nascimento[2]), int(data_de_nascimento[1]), int(data_de_nascimento[0])))
# carteira_de_trabalho = int(input('Carteira de trabalho (0 não tem): '))
# pessoa = {
#     'Nome': nome,
#     'Idade': idade,
#     'Carteira de trabalho': carteira_de_trabalho
# }

# if carteira_de_trabalho != 0:
if pessoa['Carteira de trabalho'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    # considerando que para se aposentar deve ter 35 anos de contribuição
    ano_aposentadoria = pessoa['Ano de contratação'] + 35
    pessoa['Idade aposentadoria'] = pessoa['Idade'] + (ano_aposentadoria - date.today().year)
    # pessoa['Idade aposentadoria'] = idade + (ano_aposentadoria - date.today().year)

titulos.titulo2('*', 50, ' DADOS ')

for k, v in pessoa.items():
    print(f'{k} = {v}')

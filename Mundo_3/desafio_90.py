# Dicionário em python

'''
nome = input('Nome: ').strip().capitalize()
genereo = input('Gênero [M/F]: ').strip().upper()[0]
media = float(input('Média de notas [0 a 10]: '))

if media >= 7:
    situacao = 'aprovado(a)'
elif media >= 5:
    situacao = 'em exame final'
else:
    situacao = 'reprovado(a)'

aluno = {
    'nome': nome,
    'media': media,
    'situacao': situacao
}

if genereo == 'M':
    print(f'O aluno {aluno["nome"]}, com média igual a {aluno["media"]}, está {aluno["situacao"]}.')
elif genereo == 'F':
    print(f'A aluna {aluno["nome"]}, com média igual a {aluno["media"]}, está {aluno["situacao"]}.')
'''

# OUTRO MODO

aluno = dict()

aluno['nome'] = input('Nome: ').strip().capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]} [0 a 10]: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'

for k, v in aluno.items():
    print(f'- {k} é igual a {v}')

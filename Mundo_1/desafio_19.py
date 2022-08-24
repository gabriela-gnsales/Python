# Sorteando um item na lista

from random import choice

alunos = []

for i in range(1, 5):
    aluno = input('Aluno {}: '.format(i))
    alunos.append(aluno)

aluno_sorteado = choice(alunos)

print('O aluno sorteado para apagar o quadro é o(a) {}!'.format(aluno_sorteado))

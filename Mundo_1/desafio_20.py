# Sorteando uma ordem na lista

import random

alunos = []

for i in range(1, 5):
    aluno = input('Aluno {}: '.format(i))
    alunos.append(aluno)

random.shuffle(alunos)

print('A ordem dos alunos para apresentação do trabalho é:', alunos)

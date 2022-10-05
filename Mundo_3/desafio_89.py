# Boletim com listas compostas

print('{:*^60}'.format(' CADASTRO ALUNOS E NOTAS '))

alunos = []
while True:
    nome = input('Nome: ').strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    aluno_temp = [nome, nota1, nota2]
    alunos.append(aluno_temp[:])
    aluno_temp.clear()

    continuar = input('Deseja continuar cadastrando [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida! Responda novamente:')
        continuar = input('Deseja continuar cadastrando [S/N]: ').strip().upper()[0]
    if 'N' in continuar:  # if continuar in 'N':
        break

print('{:*^60}'.format(' BOLETIM TURMA '))

print('\033[1;36m{:2}\033[m | \033[1;36m{:10}\033[m | \033[1;36m{:3}\033[m'.format('Nº', 'Nome', 'Média'))
i = 1
for aluno in alunos:
    media = (aluno[1] + aluno[2]) / 2
    print(f'{i:<2} | {aluno[0]:10} | {media:3.1f}')
    i += 1

while True:
    resp = int(input('Mostrar notas de qual aluno (informe o nº dele no boletim, para sair digite 0)? '))

    for pos, aluno in enumerate(alunos):
        if pos + 1 == resp:
            print(f'As notas de {aluno[0]} são: {aluno[1]:3.1f} e {aluno[2]:3.1f}')

    while resp not in range(1, len(alunos)):
        print('Opção inválida! Responda novamente:')
        resp = int(input('Mostrar notas de qual aluno (informe o nº dele no boletim, para sair digite 0)? '))

    if resp == 0:
        break

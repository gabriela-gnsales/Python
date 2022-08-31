# GAME: pedra, papel e tesoura

from time import sleep
from random import randint

print('-=' * 10)
print('\033[1;32mGAME: Jokenpô\033[m')
print('-=' * 10)

jogador = int(input('''Opções:
[\033[1;36m1\033[m] PEDRA
[\033[1;36m2\033[m] PAPEL
[\033[1;36m3\033[m] TESOURA
Qual a sua jogada? '''))

computador = randint(1, 3)

print('\033[7;3740mJO\033[m')
sleep(1)
print('\033[7;3740mKEN\033[m')
sleep(1)
print('\033[7;3740mPO!!!\033[m')

print(f'A opção escolhida pelo computador foi a \033[1;36m{computador}\033[m.')

# pedra ganha da tesoura -> 1 ganha 3
# tesoura ganha do papel -> 3 ganha 2
# papel ganha da pedra -> 2 ganha 1

pontuacao_jogador = 0
pontuacao_computador = 0

if jogador == 1:
    if computador == 1:
        pontuacao_jogador = 1
        pontuacao_computador = 1
        print('EMPATE!')
    elif computador == 2:
        pontuacao_jogador = 0
        pontuacao_computador = 2
        print('GANHADOR: computador!')
    else:
        pontuacao_jogador = 2
        pontuacao_computador = 0
        print('GANHADOR: jogador!')
elif jogador == 2:
    if computador == 1:
        pontuacao_jogador = 2
        pontuacao_computador = 0
        print('GANHADOR: jogador!')
    elif computador == 2:
        pontuacao_jogador = 1
        pontuacao_computador = 1
        print('EMPATE!')
    else:
        pontuacao_jogador = 0
        pontuacao_computador = 2
        print('GANHADOR: computador!')
else:
    if computador == 1:
        pontuacao_jogador = 0
        pontuacao_computador = 2
        print('GANHADOR: computador!')
    elif computador == 2:
        pontuacao_jogador = 2
        pontuacao_computador = 0
        print('GANHADOR: jogador!')
    else:
        pontuacao_jogador = 1
        pontuacao_computador = 1
        print('EMPATE!')

print(f'''\033[1;32mPLACAR:\033[m
Jogador: \033[1;36m{pontuacao_jogador}\033[m pontos.
Computador: \033[1;36m{pontuacao_computador}\033[m pontos.
''')

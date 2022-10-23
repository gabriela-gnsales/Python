# Jogo de dados

from time import sleep
from random import randint
from operator import itemgetter
import titulos

jogo = {}
# jogo = []
for i in range(4):
    jogo[f'jogador {i+1}'] = randint(1, 6)
    # jogador = {f'jogador {i+1}': randint(1, 6)}
    # jogo.append(jogador)

titulos.titulo2('-', 50, ' VALORES SORTEADOS ')

for jogador, resultado in jogo.items():
    print(f'O {jogador} tirou {resultado} no dado.')
    sleep(0.5)

# i = 1
# for jogador in jogo:
#     for k, v in jogador.items():
#         # print(f'O {k} tirou {v} no dado.')
#         print(f'O {k} {i} tirou {v} no dado.')
#         # sleep(0.7)
#     i += 1

titulos.titulo2('-', 50, ' RANKING DOS JOGADORES ')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # vira uma lista
verifica_empate = ranking[:]
jogadores_empatados = []
i = 1

for jogador in ranking:
    print(f'{i}º lugar: {jogador[0]} -> tirou {jogador[1]} no dado.')
    sleep(0.5)
    # verificando se houve empate e printar o resultado com essa informação
    cont = c = 0
    for j in verifica_empate:
        if jogador[1] == verifica_empate[c][1]:
            cont += 1
        c += 1
    if cont > 1:
        jogadores_empatados.append(jogador[0])
    i += 1

if len(jogadores_empatados) > 1:
    print('Empate entre os jogadores:', jogadores_empatados)

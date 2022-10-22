# Jogo de dados

from time import sleep
from random import randint
from operator import itemgetter
import titulos

jogo = {}
for i in range(4):
    # jogador = {f'jogador {i+1}': randint(1, 6)}
    jogo[f'jogador {i+1}'] = randint(1, 6)
    # jogador = {'jogador': randint(1, 6)}
    # jogo.copy(jogador)
    # jogo.append(jogador)
print(jogo)
# titulos.titulo2('-', 30, ' VALORES SORTEADOS ')
# i = 1
# for jogador in jogo:
#     for k, v in jogador.items():
#         # print(f'O {k} tirou {v} no dado.')
#         print(f'O {k} {i} tirou {v} no dado.')
#         # sleep(0.7)
#     i += 1
#
# titulos.titulo2('-', 30, ' RANKING DOS JOGADORES ')


ranking = {}
rankig = sorted(jogo.items(), key=itemgetter(1))
# rankig = sorted(jogo)
print(rankig)

# print(jogador.items())
# print(rankig)


# jogos = {}
# for i in range(4):
#     jogos[f'jogador {i+1}']: randint(1, 6)
#     # jogos.copy()
#     print(jogos)
#     # jogadores.append(jogador)
# print(jogos)




#     print(jogadores)
#
# print(jogadores[0].items())
# print(jogadores[0].keys())
# print(jogadores[0].values())


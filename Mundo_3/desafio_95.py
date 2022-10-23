# Aprimorando os dicionários

import pandas as pd
import titulos

titulos.titulo1('*', 50, ' CADASTRO JOGADOR DE FUTEBOL ')

jogadores = []
while True:
    nome = input('Nome do jogador: ').strip().capitalize()
    num_partidas = int(input(f'Número de partidas que {nome} jogou: '))
    gols = []
    for i in range(num_partidas):
        gols.append(int(input(f'    Quantos gols na {i+1}ª partida? ')))
    total = sum(gols)

    jogador = {
        'Nome': nome,
        'Número de partidas': num_partidas,
        'Gols': gols,
        'Total': total
    }

    jogadores.append(jogador)
    while True:
        resp = input('Deseja continuar cadastrando [S/N]? ').strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break

print('-=' * 15)

coluna = ['Nome', 'Gols', 'Total']
dados = []
# linha = []
for jogador in jogadores:
    # linha.append(jogador['Nome'])
    dados.append(jogador)

tabela = pd.DataFrame(columns=coluna, data=dados)
print(tabela)

print('-=' * 15)

programa = False
while not programa:
    # mostrar_jogador = 0
    programa = True
    while True:
        mostrar_jogador = int(input('Mostrar dados de qual jogador [insira o código dele] (para sair digite 999)? '))
        if mostrar_jogador in range(len(jogadores)):
            break
        elif mostrar_jogador == 999:
            programa = False
        # else:
        print('ERRO! Insira um código válido.')
    # if mostrar_jogador == 999:
    #     programa = False
    for indice, jogador in enumerate(jogadores):
        if indice == mostrar_jogador:
            print(f'=> Levantamento do jogador {jogador["Nome"]}:')
            if jogador['Gols']:
                i = 1
                for n_gol in jogador['Gols']:
                    print(f'No {i}º jogo fez {n_gol} gols.')
                    i += 1

titulos.titulo2('*', 50, ' PROGRAMA FINALIZADO ')

# Cadastro de jogador de futebol

import titulos

titulos.titulo2('*', 50, ' CADASTRO JOGADOR DE FUTEBOL ')

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

titulos.titulo2('*', 50, f' DADOS JOGADOR {nome.upper()} ')

print(f'O jogador {nome} jogou {num_partidas} partidas.')
for partida, num in enumerate(gols):
    print(f'=> Na {partida+1}ª partida fez {num} gols.')
print(f'Foi um total de {total} gols.')

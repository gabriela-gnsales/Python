# Palpites para a Mega-Sena

from random import randint
from time import sleep
import titulos

titulos.titulo1('=', 60, 'JOGO DA MEGA SENA')
# print('=' * 60)
# texto = 'JOGO DA MEGA SENA'
# print(f'{texto:^60}')
# print('=' * 60)

cont_jogos = 1
while True:

    num_jogos = int(input('Quantos jogos você quer sortear? '))
    qtd_num = int(input('Quantos números você quer que cada jogo tenha [6 a 15]? '))

    while qtd_num not in range(6, 16):
        qtd_num = int(input('Opção inválida! Responda um número entre 6 e 15: '))

    jogos = list()
    jogos_temp = list()

    for i in range(num_jogos):
        for j in range(qtd_num):
            n = randint(1, 60)
            while n in jogos_temp:
                n = randint(1, 60)
            jogos_temp.append(n)
        jogos.append(jogos_temp[:])
        jogos_temp.clear()

    if num_jogos > 1:
        titulos.titulo2('-', 60, f' SORTEANDO {num_jogos} JOGOS DE {qtd_num} NÚMEROS ')
        # print('{:-^60}'.format(f' SORTEANDO {num_jogos} JOGOS DE {qtd_num} NÚMEROS '))
    else:
        titulos.titulo2('-', 60, f' SORTEANDO {num_jogos} JOGO DE {qtd_num} NÚMEROS ')
        # print('{:-^60}'.format(f' SORTEANDO {num_jogos} JOGO DE {qtd_num} NÚMEROS '))

    # for jogo in jogos:
    #     sleep(0.7)
    #     print(f'Jogo {cont_jogos}: {sorted(jogo)}')
    #     cont_jogos += 1

    for jogo in jogos:
        sleep(0.7)
        jogo.sort()
        print(f'Jogo {cont_jogos}: ', end='')
        for n in jogo:
            print(f'{n:2} - ', end='')
        print()
        cont_jogos += 1

    continuar = input('Deseja sortear mais jogos [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida! Responda novamente:')
        continuar = input('Deseja sortear mais jogos [S/N]: ').strip().upper()[0]
    if 'N' in continuar:  # if continuar in 'N':
        break

titulos.titulo2('-', 60, ' BOA SORTE! ')

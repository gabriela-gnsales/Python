# Jogo do par ou ímpar

from random import randint
from time import sleep

print('*' * 21)
print('JOGO DO PAR OU ÍMPAR')
print('*' * 21)

'''
nome_jogador = input('Nome: ').strip().capitalize()

pontuacao_jogador = pontuacao_computador = 0
total = ''

while True:
    resp_jogador = input('Par ou ímpar (P/I) [digite S para sair]? ').strip().upper()[0]
    
    while resp_jogador != 'P' and resp_jogador != 'I' and resp_jogador != 'S':
        print('Opção inválida! Responda novamente:')
        resp_jogador = input('Par ou ímpar (P/I) [digite S para sair]? ').strip().upper()[0]

    if resp_jogador == 'S':
        break

    n_jogador = int(input('Diga um valor de 1 a 10: '))

    print('PROCESSANDO...')
    sleep(1)

    n_computador = randint(1, 10)

    print('-' * 21)

    soma = n_jogador + n_computador

    if soma % 2 == 0:
        total = 'PAR'
        if resp_jogador in 'P':
            pontuacao_jogador += 1
            print('Você VENCEU!')
        else:
            pontuacao_computador += 1
            print('Você PERDEU!')
    else:
        total = 'ÍMPAR'
        if resp_jogador in 'I':
            pontuacao_jogador += 1
            print('Você VENCEU!')
        else:
            pontuacao_computador += 1
            print('Você PERDEU!')

    print(f'Você jogou {n_jogador} e o computador {n_computador}. O total, {soma}, deu {total}.')

    print('-' * 21)

print('*' * 21)
print('FIM')
print('*' * 21)

print(f'PLACAR:\n{nome_jogador}: {pontuacao_jogador}\nComputador: {pontuacao_computador}')
'''
# OUTRO MODO

v = 0
while True:
    jogador = int(input('Diga um valor de 1 a 10: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou ímpar (P/I)? ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} -> ', end='')
    print('deu PAR!' if total % 2 == 0 else 'deu ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('-' * 30)
    print('Vamos jogar novamente...')
print('-' * 30)
print(f'GAME OVER! Você venceu {v} vezes.')

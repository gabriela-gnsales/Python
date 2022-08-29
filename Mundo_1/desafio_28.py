# Jogo da adivinhação v.1.0

import random
from time import sleep

# n = random.randrange(0, 6)

computador = random.randint(0, 5)  # Faz o computador "pensar"

# print('nº computador: ', computador)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('PARABÉNS, você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}.')

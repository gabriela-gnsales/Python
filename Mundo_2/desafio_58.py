# Jogo da adivinhação v.2.0

from random import randint
from time import sleep

print('=-' * 10)
print('\033[7;36;40mJOGO DA ADIVINHAÇÃO\033[m')
print('=-' * 10)

max = 10

computador = randint(1, max)

resposta = 's'

while resposta == 's':

    print(f'Vou pensar em um número entre 0 e {max}. Tente adivinhar...')

    jogador = int(input('Em que número eu pensei? '))

    palpites = 0

    while jogador != computador:
        print('\033[7;37;40mPROCESSANDO...\033[m')
        sleep(1)
        print('\033[7;37;40mERROU!\033[m Tente novamente!')
        palpites += 1
        if jogador > computador:
            print('\033[7;37;40mDICA:\033[m o número sorteado é \033[7;3740mMENOR\033[m que esse.')
        else:
            print('\033[7;37;40mDICA:\033[m o número sorteado é \033[7;3740mMAIOR\033[m que esse.')
        jogador = int(input('Qual número você acha que o computador sorteou? '))

    print(f'\033[7;37;40mACERTOU!\033[m O número sorteado foi o {computador} :)')

    if palpites == 1:
        print(f'Foi necessário apenas 1 palpite para vencer.')
    else:
        print(f'Foram necessários {palpites} palpites para vencer.')

    resposta = input('Quer continuar jogando [S/N]: ').strip().lower()

    while resposta != 's' and resposta != 'n':
        print('\033[7;37;40mOpção inválida!\033[m')
        resposta = input('Quer continuar jogando [S/N]: ').strip().lower()

    computador = randint(1, max)

print('=-' * 10)
print('\033[7;37;40mFIM DO JOGO\033[m')
print('=-' * 10)
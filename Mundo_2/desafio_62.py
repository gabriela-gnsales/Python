# Progressão aritmética v.3.0

a_1 = int(input('Primeiro termo da P.A.: '))
r = int(input('Razão da P.A.: '))
# n = int(input('Qual termo da P.A. você quer saber o valor? '))
num = int(input('Quantos termos da P.A. você quer ver? '))
'''
print('-=' * 50)

while n != 0:
    i = 1
    a_i = a_1
    while i < n:
        a_i += r
        i += 1
    print(f'A_{n} = {a_i}')
    n = int(input('Quer saber o valor de mais algum termo da P.A. (para sair digite 0)? '))
print('FIM')
'''
'''
print('-=' * 30)

resp = False
while not resp:
# resp = True
# while resp == True:
    i = j = 1
    a_i = a_1
    while j <= num:
        print(f'\33[0;34m{j:>2}º\33[m -> ', end='')
        # print(' - ' if j < num else '', end='')
        j += 1
    print('PAUSA')
    while i <= num:
        print(f'\33[0;32m{a_i:^3}\33[m -> ', end='')
        # print(a_i, end='')
        # print(' - ' if i < num else '', end='')
        a_i += r
        i += 1
    print('PAUSA')
    resposta = input('Quer ver mais termos dessa P.A. [S/N]? ').strip().lower()[0]
    while resposta != 's' and resposta != 'n':
        print('Opção inválida! Responda novamente: ', end='')
        resposta = input('\nQuer ver mais termos dessa P.A. [S/N]? ').strip().lower()[0]
    if resposta == 's':
        num2 = int(input('Mais quantos termos da P.A. você quer ver? '))
        a_i = a_1 + (num - 1) * r
        # print('a_i:', a_i)
        num += num2
        # print('num:', num)
    else:
        # resp = False
        resp = True
print('-=' * 30)
print('FIM')
'''
print('-=' * 30)

i = j = 1
a_i = a_1
total = 0
mais = num

resp = True
while resp == True:
    total += mais
    while j <= total:
        print(f'\33[0;34m{j:>2}º\33[m -> ', end='')
        j += 1
    print('PAUSA')
    while i <= total:
        print(f'\33[0;32m{a_i:^3}\33[m -> ', end='')
        a_i += r
        i += 1
    print('PAUSA')
    resposta = input('Quer ver mais termos dessa P.A. [S/N]? ').strip().lower()[0]
    while resposta != 's' and resposta != 'n':
        print('Opção inválida! Responda novamente: ', end='')
        resposta = input('\nQuer ver mais termos dessa P.A. [S/N]? ').strip().lower()[0]
    if resposta == 's':
        mais = int(input('Mais quantos termos da P.A. você quer ver? '))
        # i = j = 1  # se quiser ver os termos da P.A. desde o primeiro valor
    else:
        resp = False
print('-=' * 30)
print('FIM')

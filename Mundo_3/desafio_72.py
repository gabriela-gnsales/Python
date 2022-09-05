# Número por extenso

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    while True:
        n = int(input('Digite um valor entre 0 e 10: '))
        if 0 <= n <= 10:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {tupla[n]}.')
    resp = input('Deseja continuar [S/N]? ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if resp == 'N':
        break
print('FIM')
'''
n = int(input('Digite um valor entre 0 e 10: '))
while n not in range(0, 11):
    n = int(input('Tente novamente. Digite um valor entre 0 e 10: '))

for i in range(len(tupla)):
    if i == n:
        print(f'Você digitou o número {tupla[i]}.')

for pos, elemento in enumerate(tupla):
    if pos == n:
        print(f'Você digitou o número {elemento}.')
'''

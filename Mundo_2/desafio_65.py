# Maior e menor valores

resp = 'S'
i = soma = maior = 0
menor = 999

while resp == 'S':

    n = int(input(f'\033[1;34;40m{i + 1}º valor:\033[m '))
    resp = input('Quer continuar [S/N]? ').strip().upper()

    while resp != 'S' and resp != 'N':
        print('Opção inválida!')
        resp = input('Quer continuar [S/N]? ').strip().upper()

    soma += n
    i += 1

    if n > maior:
        maior = n

    if n < menor:
        menor = n

print('\033[1;34m-\033[m' * 50)

print(f'A média dos \033[1;34;40m{i}\033[m valores é \033[1;34;40m{(soma / i):.1f}\033[m.')
print(f'O menor valor digitado foi \033[1;34;40m{menor}\033[m e o maior foi \033[1;34;40m{maior}\033[m.')

print('\033[1;34m-\033[m' * 50)

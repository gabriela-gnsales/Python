# Criando um menu de opções

n1 = float(input(f'Valor 1: '))
n2 = float(input(f'Valor 2: '))

resposta = 0

while resposta != 5:
    print('-' * 22)
    print('''OPÇÕES:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    print('-' * 22)
    resposta = int(input('Qual sua opção: '))

    while resposta != 1 and resposta != 2 and resposta != 3 and resposta != 4 and resposta != 5:
        print('Opção inválida! Tente novamente.')
        resposta = int(input('Qual sua opção: '))

    if resposta == 1:
        print(f'Soma: {n1} + {n2} = {n1 + n2}')
    elif resposta == 2:
        print(f'Multiplicação: {n1} * {n2} = {(n1 * n2):.1f}')
    elif resposta == 3:
        maior = n1
        menor = n2
        if n2 > maior:
            maior = n2
            menor = n1
        print(f'Maior: {maior} > {menor}')
    elif resposta == 4:
        n1 = float(input(f'Valor 1: '))
        n2 = float(input(f'Valor 2: '))

print('-' * 22)
print('FIM')

# Análise de dados do grupo

print('*' * 22, 'CADASTRO', '*' * 22)

tot_18 = tot_H = tot_M_20 = 0

while True:

    idade = int(input('Idade: '))

    genero = ' '
    while genero not in 'MF':
        genero = input('Gênero [M/F]: ').strip().upper()[0]

    # while genero != 'M' and genero != 'F':
    #     print('Opção inválida! Responda novamente:')
    #     genero = input('Gênero [M/F]: ').strip().upper()[0]

    if idade >= 18:
        tot_18 += 1

    if genero == 'M':
        tot_H += 1

    if genero == 'F' and idade < 20:
        tot_M_20 += 1

    resposta = input('Deseja cadastrar mais alguém [S/N]? ').strip().upper()[0]

    while resposta != 'S' and resposta != 'N':
        print('Opção inválida! Responda novamente:')
        resposta = input('Deseja cadastrar mais alguém [S/N]? ').strip().upper()[0]

    if resposta == 'N':
        break

print('*' * 20, 'FIM DO CADASTRO', '*' * 20)

print(f'{tot_18} pessoas têm 18 anos ou mais.\nForam cadastrados {tot_H} homens.\n{tot_M_20} mulheres têm menos de 20 anos.')

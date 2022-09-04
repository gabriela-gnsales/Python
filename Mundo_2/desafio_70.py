# Estatísticas em produtos

print('*' * 20, 'CADASTRO PRODUTOS', '*' * 20)

print('{:-^40}'.format(' CADASTRO PRODUTOS '))

total = tot_mil = menor_preco = i = 0
produto_menor_preco = ''

while True:

    produto = input('Nome do produto: ').strip().lower()
    preco = float(input('Preço: R$ '))

    total += preco

    if preco > 1000:
        tot_mil += 1

    if i == 0 or preco < menor_preco:
        produto_menor_preco = produto
        menor_preco = preco

    i += 1

    resposta = input('Deseja continuar cadastrando produtos [S/N]? ').strip().upper()[0]

    while resposta != 'S' and resposta != 'N':
        print('Opção inválida! Responda novamente:')
        resposta = input('Deseja continuar cadastrando produtos [S/N]? ').strip().upper()[0]

    if resposta == 'N':
        break

print('*' * 20, 'FIM DO CADASTRO', '*' * 20)

print(f'O total gasto na compra foi de R$ {total:.2f}.')

if tot_mil == 1:
    print('Apenas 1 produto custa mais de R$ 1000.00.')
elif tot_mil > 1:
    print(f'{tot_mil} produtos custam mais de R$ 1000.00.')
else:
    print('Nenhum produto custa mais de R$ 1000.00.')

print(f'O produto mais barato foi {produto_menor_preco} que custa R$ {menor_preco:.2f}.')

# lista de preços com tupla

produtos = 'pão', 3.5, 'café', 18, 'leite', 6.4, 'queijo', 22

print(produtos)

print('=' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('=' * 40)

for produto in produtos:
    if type(produto) == str:
        print(f'{produto.capitalize():.<30}', end=' ')
    else:
    # if type(produto) == int or type(produto) == float:
        print(f'R$ {produto:>5.2f}')

print('=' * 40)

####

print('_' * 20)
print('{:5} | {:5}'.format('Produto', 'Preço'))
for produto in produtos:
    if type(produto) == str:
        print(f'{produto:6}  |', end=' ')
    if type(produto) == int or type(produto) == float:
        print(f'R$ {produto:>5.2f}')
print('_' * 20)

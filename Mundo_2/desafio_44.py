# Gerenciador de pagamentos

print('{:=^40}'.format(' LOJAS GUANABARA '))

preco_normal = float(input('Preço normal: R$ '))
condicao_pagamento = int(input('''Informe a condição de pagamento:
\033[1;31m*\033[m \033[1;36m1\033[m à vista dinheiro/cheque: 10% de desconto
\033[1;31m*\033[m \033[1;36m2\033[m à vista no cartão: 5% de desconto
\033[1;31m*\033[m \033[1;36m3\033[m 2x no cartão: preço normal 
\033[1;31m*\033[m \033[1;36m4\033[m 3x ou mais no cartão: 20% de juros 
'''))

if condicao_pagamento == 1:
    preco_novo = preco_normal - preco_normal * 0.1
    print(f'Preço a pagar: R$ {preco_novo}.')
elif condicao_pagamento == 2:
    preco_novo = preco_normal - preco_normal * 0.05
    print(f'Preço a pagar: R$ {preco_novo}.')
elif condicao_pagamento == 3:
    parcela = preco_normal / 2
    print(f'Preço a pagar: R$ {preco_normal}, dividido em 2 parcelas de R$ {parcela:.02f}.')
else:
    n_parcela = int(input('Informe o nº de parcelas: '))
    preco_novo = preco_normal + preco_normal * 0.2
    parcela = preco_novo / n_parcela
    print(f'Preço a pagar: R$ {preco_novo}, dividido em {n_parcela} parcelas de R$ {parcela:.02f}.')

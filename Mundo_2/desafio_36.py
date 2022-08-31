# Aprovando empréstimo

from math import ceil

valor_casa = float(input('Valor da casa: R$ '))
salario_comprador = float(input('Salário do comprador: R$ '))
qntd_anos_pagar = int(input('Quantidade de anos do financiamento: '))

prestacao_mensal = valor_casa / (qntd_anos_pagar * 12)
maximo_parcela = 0.3 * salario_comprador

if prestacao_mensal > maximo_parcela:
    nova_qntd_anos_pagar = valor_casa / maximo_parcela
    print(f'Empréstimo NEGADO! O valor da prestação mensal, R$ {prestacao_mensal:.02f}, é maior do que 30% do seu salário (R$ {maximo_parcela:.02f}).')  # , end=' '
    print(f'Para comprar esse imóvel, considerando seu salário atual, você necessitaria pagá-lo em {ceil(nova_qntd_anos_pagar)} meses ({ceil(nova_qntd_anos_pagar / 12)} anos).')
else:
    print(f'Empréstimo pode ser CONCEDIDO! O valor da prestação mensal é de R$ {prestacao_mensal:.02f}.')

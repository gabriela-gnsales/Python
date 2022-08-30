# Aprovando empréstimo

from math import ceil

valor_casa = float(input('Valor da casa: R$ '))
salario_comprador = float(input('Salário do comprador: R$ '))
qntd_anos_pagar = int(input('Quantidade de anos para pagar: '))

prestacao_mensal = valor_casa / (qntd_anos_pagar * 12)
percentual_salario = 0.3 * salario_comprador

if prestacao_mensal > percentual_salario:
    nova_qntd_anos_pagar = valor_casa / percentual_salario
    print(f'Empréstimo negado! O valor da prestação mensal, R$ {prestacao_mensal:.02f}, é maior do que 30% do seu salário (R$ {percentual_salario:.02f}).')
    print(f'Para comprar esse imóvel, considerando seu salário atual, você necessitaria pagá-lo em {ceil(nova_qntd_anos_pagar)} meses ({ceil(nova_qntd_anos_pagar / 12)} anos).')
else:
    print(f'Parabéns, você acaba de adquirir esse imóvel! O valor da prestação mensal é de R$ {prestacao_mensal:.02f}.')

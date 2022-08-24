# Aluguel de carros

km_percorrido = float(input('Quantos km foram percorridos? '))
dias_alugado = int(input('Por quantos dias o carro foi alugado? '))

preco = km_percorrido * 0.15 + dias_alugado * 60

print('O preço do aluguel desse carro foi R$ {:.2f}'.format(preco))

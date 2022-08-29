# Custo da viagem

distancia = float(input('Qual a distância da sua viagem em km? '))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f'O preço da sua viagem é de R$ {preco:.2f}.')

# OUTRO MODO COM IF-ELSE SIMPLIFICADO

preco2 = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print(f'Preço calculado por outro modo: R$ {preco2:.2f}.')

# Separando dígitos de um nº

n = int(input('Digite um número de 0 a 9999: '))

print('TRATANDO COMO NÚMERO')

print(f'Unidade: {n % 10}')  # n // 1 % 10
print(f'Dezena: {(n % 100) // 10}')  # n // 10 % 10
print(f'Centena: {(n % 1000) // 100}')  # n // 100 % 10
print(f'Milhar: {n // 1000}')  # n // 1000 % 10

print('TRATANDO COMO STRING -> só dá certo se o nº tiver 4 dígitos (sem usar if else)')

# num = str(n)
#
# print(f'Unidade: {num[3]}')
# print(f'Dezena: {num[2]}')
# print(f'Centena: {num[1]}')
# print(f'Milhar: {num[0]}')

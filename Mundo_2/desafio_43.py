# Índice de massa corporal

peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))

imc = peso / altura ** 2

print(f'IMC: {imc:.01f}.')

if imc < 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc <= 30:
    print('Sobrepeso.')
elif imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')

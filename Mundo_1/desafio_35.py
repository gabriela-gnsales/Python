# Analisando triângulo v.1.0

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)

lado1 = float(input('Qual o comprimento do lado 1 do triângulo? '))

lado2 = float(input('Qual o comprimento do lado 2 do triângulo? '))

lado3 = float(input('Qual o comprimento do lado 3 do triângulo? '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('\033[0;30mÉ triângulo!\033[m')
else:
    print('\033[7;30mNão é triângulo!\033[m')

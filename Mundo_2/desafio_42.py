# Analisando triângulos v.2.0

print('-=' * 20)
print('\033[1;32mAnalisador de triângulos\033[m')
print('-=' * 20)

lado1 = float(input('Qual o comprimento do lado 1 do triângulo? '))
lado2 = float(input('Qual o comprimento do lado 2 do triângulo? '))
lado3 = float(input('Qual o comprimento do lado 3 do triângulo? '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('\033[1;34mÉ triângulo!\033[m')
    if lado1 == lado2 == lado3:
        print('Equilátero.')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Isósceles.')
    else:
        print('Escaleno.')
else:  # lado1 != lado2 != lado3 != lado1
    print('\033[1;31mNão é triângulo!\033[m')

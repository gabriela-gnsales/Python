# Maior e menor valores

n1 = float(input('Informe o 1º nº: '))
n2 = float(input('Informe o 2º nº: '))
n3 = float(input('Informe o 3º nº: '))

if n1 > n2:
    if n1 > n3:
        maior = n1
        if n2 > n3:
            menor = n3
        else:
            menor = n2
    else:
        maior = n3
        menor = n2
else:
    if n2 > n3:
        maior = n2
        if n1 > n3:
            menor = n3
        else:
            menor = n1
    else:
        maior = n3
        menor = n1

print(f'O maior número é {maior} e o menor é {menor}.')

# OUTRO MODO

# Verificando quem é menor (min)

min = n1

if n2 < n1 and n2 < n3:
    min = n2
elif n3 < n1 and n3 < n2:
    min = n3

# Verificando quem é maior (max)

max = n2

if n1 > n2 and n1 > n3:
    max = n1
elif n3 > n1 and n3 > n2:
    max = n3

print(f'O maior número é {max} e o menor é {min}.')

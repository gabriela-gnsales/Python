# Maior e menor da sequência
'''
maior = 0
menor = 999
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso é {maior} kg.\nO menor peso é {menor} kg.')
'''
print('-=' * 20)

# OUTRO MODO

menor = maior = 0
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso é {maior} kg.\nO menor peso é {menor} kg.')

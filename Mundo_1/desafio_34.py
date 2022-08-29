# Aumentos múltiplos

salario = float(input('Informe seu salário: R$ '))

if salario > 1250:
    aumento = 10
else:
    aumento = 15

salario_novo = salario * (aumento / 100 + 1)

print(f'Seu salário teve um aumento de {aumento}% e agora é R$ {salario_novo:.2f}.')

# if salario > 1250:
#     aumento = 0.1
# else:
#     aumento = 0.15
#
# salario_novo = salario * (aumento + 1)
#
# print(f'Seu salário teve um aumento de {int(aumento * 100)}% e agora é R$ {salario_novo:.2f}.')

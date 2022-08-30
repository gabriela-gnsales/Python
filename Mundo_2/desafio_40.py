# Aquele clássico da média

nota1 = float(input('1º nota: '))
nota2 = float(input('2º nota: '))

media = (nota1 + nota2) / 2

print(f'Sua média foi de {media:.01f}.')

if media < 5:
    print('Reprovado.')
elif 5 <= media < 7:
    print('Recuperação.')
else:
    print('Aprovado.')

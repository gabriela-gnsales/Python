# Vários números com flag

i = s = 0
while True:
    n = int(input(f'Digite o {i + 1}º número inteiro [para sair digite 999]: '))
    if n == 999:
        break
    s += n
    i += 1
print('*' * 60)
print(f'Foram digitados {i} números e a soma deles é {s}.')

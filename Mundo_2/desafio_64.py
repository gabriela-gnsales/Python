# Tratando vários valores v.1.0

n = s = i = 0
while n != 999:
    n = int(input(f'{i + 1}º valor (para parar digite 999): '))
    if n != 999:
        s += n
        i += 1
print(f'Foram digitados {i} números e a soma deles é {s}.')

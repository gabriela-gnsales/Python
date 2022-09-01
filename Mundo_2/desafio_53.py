# Detector de palíndromo

frase = input('Digite uma frase: ').strip().replace(' ', '').lower()

print('-=' * 20)

# quando precisa tirar espaços extras no meio da frase
# frase_2 = input('Digite uma frase: ').strip().lower().split()
# frase_2_n = ' '.join(frase_2)
# print('Frase 2:', frase_2_n)

print('Frase:', frase)
frase_invertida = frase[::-1]
print('Frase invertida:', frase_invertida)

c = 0
for i in range(0, len(frase)):
    if frase[i] == frase_invertida[i]:
        c += 1
if c == len(frase):
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO é um palíndromo!')

print('-=' * 20)

# OUTRO MODO
inverso = ''
for letra in range(len(frase)-1, -1, -1):
    inverso += frase[letra]
print(frase, '->', inverso)

if inverso == frase:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO é um palíndromo!')

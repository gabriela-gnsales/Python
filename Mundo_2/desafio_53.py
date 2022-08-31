# Detector de palíndromo

frase = input('Digite uma frase: ').strip().replace(' ', '').lower()

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

# for i in range(len(frase)-1, -1, -1):
#     print(frase[i])

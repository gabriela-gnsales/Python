# Maior e menor valores em tupla

from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Tupla:', n)

print('-' * 25)

print('Maior:', max(n))
print('Menor:', min(n))

print('-' * 25)

maior = menor = n[0]
for i in n:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print('Maior:', maior)
print('Menor:', menor)

print('-' * 25)

maior = menor = n[0]
for i in range(len(n)):
    if n[i] > maior:
        maior = n[i]
    if n[i] < menor:
        menor = n[i]
print('Maior:', maior)
print('Menor:', menor)

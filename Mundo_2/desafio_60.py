# Cálculo do fatorial

n = int(input('Quer saber o fatorial de qual número? '))

# --------------- #

fatorial_for = 1

for i in range(n, 1, -1):
    fatorial_for *= i

print(f'Fatorial FOR: {n}! = {fatorial_for}')

# --------------- #

fatorial_while = 1
c = n

while c > 0:
    fatorial_while *= c
    c -= 1

print(f'Fatorial WHILE: {n}! = {fatorial_while}')

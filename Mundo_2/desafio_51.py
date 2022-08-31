# Progressão aritmética

a_1 = int(input('Primeiro termo da P.A.: '))
r = int(input('Razão da P.A.: '))

for n in range(1, 11):
    a_n = a_1 + (n-1) * r
    print(f'a_{n} = {a_n}')

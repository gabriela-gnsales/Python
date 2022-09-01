# Progressão aritmética v.2.0

a_1 = int(input('Primeiro termo da P.A.: '))
r = int(input('Razão da P.A.: '))
n = int(input('Qual termo da P.A. você quer saber o valor? '))
'''
for n in range(1, 11):
    a_n = a_1 + (n-1) * r
    print(f'a_{n} = {a_n}')
'''
c = a_n = 1

while c < n:
    a_n = a_1 + c * r
    # print(a_n)
    c += 1

print(f'a_{n} = {a_n}')

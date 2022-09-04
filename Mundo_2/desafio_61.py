# Progressão aritmética v.2.0

a_1 = int(input('Primeiro termo da P.A.: '))
r = int(input('Razão da P.A.: '))
n = int(input('Qual termo da P.A. você quer saber o valor? '))
num = int(input('Qual o nº de termos da P.A. você quer ver? '))

c = a_n = 1
while c < n:
    a_n = a_1 + c * r
    # print(a_n)
    c += 1
print(f'A_{n} = {a_n}')

print('-' * 30)

i = 0
a_i = a_1
while i < num:
    print(f'{a_i} -> ', end='')
    a_i += r
    i += 1
print('FIM')

print('-' * 30)

for l in range(1, num+1):
    print(f'\33[0;34m{l:>2}º\33[m -> ', end='')
print('\33[0;34mFIM\33[m')

a_n = a_1 + (num - 1) * r
# print(a_n)
for j in range(a_1, a_n + r, r):
    print(f'{j:^3} \33[0;31m->\33[m ', end='')
print('FIM')

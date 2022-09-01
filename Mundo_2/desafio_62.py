# Progressão aritmética v.3.0

a_1 = int(input('Primeiro termo da P.A.: '))
r = int(input('Razão da P.A.: '))
n = int(input('Qual termo da P.A. você quer saber o valor? '))

while n != 0:

    c = a_n = 1

    while c < n:
        a_n = a_1 + c * r
        # print(a_n)
        c += 1

    print(f'a_{n} = {a_n}')

    n = int(input('Quer saber o valor de mais algum termo da P.A. (para sair digite 0)? '))

print('FIM')

# Sequência de Fibonacci v.1.0

print('-' * (len('Sequência de Fibonacci')+1))
print('Sequência de Fibonacci')
print('-' * (len('Sequência de Fibonacci')+1))

num = int(input('Quantos termos você quer mostrar? '))

print('~' * (len('Sequência de Fibonacci')+1))

i = n1 = 0
n2 = 1
while i < num:
    if i == 0 or i == 1:
        n = i
    else:
        n = n1 + n2
    print(n, '-> ', end='')
    n1 = n2
    n2 = n
    i += 1
print('FIM')

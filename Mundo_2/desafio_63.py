# Sequência de Fibonacci v.1.0

n = int(input('Informe um número inteiro: '))
print('-' * (len('Sequência de Fibonacci')+1))
print('Sequência de Fibonacci')
print('-' * (len('Sequência de Fibonacci')+1))
i = -1
while i < n:
    if i == -1 or i == 0:
        f_i = 1
    elif i == 1:
        f_i = 2
    else:
        f_i = (i-1) + (i-2)
    print(f_i)
    i += 1

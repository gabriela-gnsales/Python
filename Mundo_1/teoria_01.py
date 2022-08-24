# Operações aritméticas

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

s = n1 + n2  # soma
m = n1 * n2  # multiplicação
d = n1 / n2  # divisão
di = n1 // n2  # divisão inteira
r = n1 % n2  # resto da divisão
e1 = n1 ** n2  # exponenciação
e2 = pow(n1, n2)  # exponenciação fórmula

print('A soma é {}, \n o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end=' ')
print('Divisão inteira {}, resto da divisão {}, potência (forma 1) {} e potência (forma 2) {}'.format(di, r, e1, e2))
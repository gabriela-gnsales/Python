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

print('EX IF-ELSE SIMPLIFICADO')
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')

# FORMATAÇÃO STRING
print('{:-^40}'.format(' TÍTULO '))

'''
CORES

\033[ código estilo ; código texto ; código background (fundo) m

Estilo:
    0 = none
    1 = bold
    4 = underline
    7 = negative (inverte)
    
Texto:
    30 = branco
    31 = vermelho
    32 = verde
    33 = amarelo
    34 = azul
    35 = lilás
    36 = ciano
    37 = cinza
    
Fundo:
    40 = branco
    41 = vermelho
    42 = verde
    43 = amarelo
    44 = azul
    45 = lilás
    46 = ciano
    47 = cinza

'''
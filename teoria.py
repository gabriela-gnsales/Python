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

# TUPLAS: () ou sem nada
# LISTAS: []
# DICIONÁRIOS: {}

lanche = 'hambúrguer', 'batata', 'suco', 'sorvete'

lanche = 'hambúrguer', 'batata', 'suco', 'sorvete'
lanche2 = ('hambúrguer', 'batata', 'suco', 'sorvete')

print(lanche)
print(lanche2)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('Comi pra caramba!')

print(sorted(lanche))

tupla1 = 1, 2, 3
tupla2 = 4, 5, 6,
print('tupla1 + tupla2 =', tupla1 + tupla2)
print('tupla2 + tupla1 =', tupla2 + tupla1)
print('tupla2 + tupla2 =', tupla2 + tupla2)
print('2 * tupla1 =', 2 * tupla1)
print('Índice (posição) do número 3 na tupla1:', tupla1.index(3))
print('Quantidade de números 5 na tupla2:', tupla2.count(5))

lanche3 = ['hambúrguer', 'batata', 'suco', 'sorvete']
lanche3.append('bolo')

lanche3 = ['hambúrguer', 'batata', 'suco', 'sorvete']
print(lanche3)

lanche3.append('bolo')
print(lanche3)

lanche3.insert(1, 'bala')
print(lanche3)

del lanche3[3]
print(lanche3)

lanche3.pop()
print(lanche3)

lanche3.pop(0)
print(lanche3)

lanche3.append('pão')
print(lanche3)

lanche3.remove('pão')
print(lanche3)

valores = list(range(4, 11))
print(valores)

valores.sort(reverse=True)

print(valores)

# LISTA VAZIA
lista = []
lista = list()

# LIGAÇÃO DE 2 LISTAS
a = [1, 2, 3]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# CÓPIA DE UMA LISTA

c = a[:]
print(f'Lista C: {c}')
c[2] = 12
print(f'Lista A: {a}')
print(f'Lista C: {c}')

galera = list()
dado = []
for c in range(3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print('galera:', galera)

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
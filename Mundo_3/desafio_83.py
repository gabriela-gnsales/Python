# Validando expressões matemáticas

expressao = input('Digite a expressão: ').strip().lower()
# print(expressao)

c = 0
# for i in lista:
for i in expressao:
    if i == '(':
        c += 1
    elif i == ')':
        c -= 1
    if c < 0:
        break

# print('c1:', c1)
# print('c2:', c2)

if c == 0:
    print('\033[0;32mSua expressão está correta!\033[m')
else:
    print('\033[0;31mSua expressão está errada!\033[m')

# OUTRO MODO -> COM LISTA

lista = []
for simb in expressao:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('\033[0;32mSua expressão está válida!\033[m')
else:
    print('\033[0;31mSua expressão está inválida!\033[m')

# if "(" in lista and ")" in lista:
# if "(" in lista:
#     print('Há parênteses.')
# else:
#     print('Não há parênteses.')
#
# if 'a' in lista or 'b' in lista:
#     print("Há 'a' e/ou 'b'.")
# else:
#     print("Não há 'a' nem 'b'.")

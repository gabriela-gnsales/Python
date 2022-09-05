# Contando vogais em tupla

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar')
# vogais = 'a', 'e', 'i', 'o', 'u'

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as seguintes vogais:', end=' ')
    for letra in palavra.upper():
        if letra in 'AEIOU':
            print(letra, end=' ')
    # for vogal in vogais:
    #     if vogal in palavra:
    #         print(vogal.upper(), end=' ')

def titulo1(simbolo, numero, texto):
    print(simbolo * numero)
    print(f'{texto:^{numero}}')
    print(simbolo * numero)


def titulo2(simbolo, numero, texto):
    print(f'{texto:{simbolo}^{numero}}')

def titulo1(simbolo, numero, texto):  # MUDAR PARÂMETROS PARA: texto, simbolo='-', numero=50
    print(simbolo * numero)
    print(f'{texto:^{numero}}')
    print(simbolo * numero)


def titulo2(simbolo, numero, texto):  # MUDAR PARÂMETROS PARA: texto, simbolo='-', numero=50
    print(f'{texto:{simbolo}^{numero}}')

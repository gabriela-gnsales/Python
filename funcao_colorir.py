  # \033[código estilo; código texto; código background(fundo) m

# SEM CÓDIGO DE COR DO FUNDO

def colorir1(msg, estilo='negrito', cor='branco'): 
    cod_estilo = {
        'nenhum': 0,
        'negrito': 1,
        'underline': 4,
        'inverso': 7
    }

    cod_texto = {
        'branco': 30,
        'vermelho': 31,
        'verde': 32,
        'amarelo': 33,
        'azul': 34,
        'lilas': 35,
        'ciano': 36,
        'cinza': 37
    }
    msg = f'\033[{cod_estilo[estilo]};{cod_texto[cor]}m{msg}\033[m'
    return msg


# COM CÓDIGO DE COR DO FUNDO

def colorir1(msg, estilo='negrito', cor='branco', fundo='branco'):
    cod_estilo = {
        'nenhum': 0,
        'negrito': 1,
        'underline': 4,
        'inverso': 7
    }
    cod_texto = {
        'branco': 30,
        'vermelho': 31,
        'verde': 32,
        'amarelo': 33,
        'azul': 34,
        'lilas': 35,
        'ciano': 36,
        'cinza': 37
    }
    cod_fundo = {
        'branco': 40,
        'vermelho': 41,
        'verde': 42,
        'amarelo': 43,
        'azul': 44,
        'lilas': 45,
        'ciano': 46,
        'cinza': 47
    }
    msg = f'\033[{cod_estilo[estilo]};{cod_texto[cor]};{cod_fundo[fundo]}m{msg}\033[m'
    return msg
    
# Verificando as primeiras letras de um texto

cidade = input('Digite o nome de uma cidade: ').upper().strip()

cidade_dividido = cidade.split()

print(cidade_dividido[0])

if cidade_dividido[0].upper() == 'SANTO':
    print('O nome dessa cidade começa com a palavra SANTO!')
else:
    print('O nome dessa cidade NÃO começa com a palavra SANTO!')

print(f'O nome dessa cidade começa com a palavra SANTO? {cidade_dividido[0] == "SANTO"}')

# OUTRO MODO

print(cidade[:5] == 'SANTO')

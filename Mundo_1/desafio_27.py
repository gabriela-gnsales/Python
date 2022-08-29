# Primeiro e último nome de uma pessoa

nome = input('Informe seu nome completo: ').strip()

nome_dividido = nome.split()
primeiro_nome = nome_dividido[0]
tamanho_nome_dividido = len(nome_dividido)
print(f'Tamanho: {tamanho_nome_dividido} Tipo: {type(tamanho_nome_dividido)}')
ultimo_nome = nome_dividido[tamanho_nome_dividido - 1]

ultimo_nome_2 = nome_dividido[-1]

print('Primeiro nome:', primeiro_nome)
print('Último nome:', ultimo_nome)
print('Último nome 2:', ultimo_nome_2)

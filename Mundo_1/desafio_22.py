# Analisador de textos

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Nome com todas as letras maiúsculas: {nome.upper()}.')

print(f'Nome com todas as letras minúsculas: {nome.lower()}.')

nome_sem_espaco = nome.replace(" ", "")

print(f'Nome sem espaços: {nome_sem_espaco}.')

print(f'Número total de letras (sem considerar espaços): {len(nome_sem_espaco)}.')

print(f'Número total de letras (sem considerar espaços -> OUTRO MODO): {len(nome) - nome.count(" ")}.')

nome_dividido = nome.split()
primeiro_nome = nome_dividido[0]

print(f'Primeiro nome: {primeiro_nome}.')
print(f'Número de letras do primeiro nome: {len(primeiro_nome)}.')

print(f'Número de letras do primeiro nome (OUTRO MODO): {nome.find(" ")}.')

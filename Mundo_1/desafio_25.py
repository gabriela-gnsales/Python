# Procurando uma string dentro de outra

nome = input('Informe seu nome completo: ').strip()

print(f'Seu nome tem a palavra SILVA? {"silva" in nome.lower()}.')

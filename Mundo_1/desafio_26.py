# Primeira e última ocorrência de uma string

frase = input('Escreva uma frase: ').strip().upper()

n = frase.count("A")

if n > 1:
    print(f'A letra A aparece {n} vezes nessa frase.')
elif n == 1:
    print(f'A letra A aparece {n} vez nessa frase.')
else:
    print('Nessa frase não há nenhuma letra A!')

frase_invertida = frase[::-1]
print('Frase invertida: ', frase_invertida)

if n >= 1:
    print(f'A primeira letra A apareceu na posição {frase.find("A") + 1}.')
    print(f'A última letra A apareceu na posição {frase.rfind("A") + 1}.')  # rfind procura a partir do lado direito

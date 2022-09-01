# Progressão aritmética

primeiro = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão da P.A.: '))
num_termos = int(input('Número de termos da P.A. a serem exibidos: '))

termo_n = primeiro + (num_termos - 1) * razao
for n in range(primeiro, termo_n + razao, razao):
    print(n, end=' -> ')
print('ACABOU')

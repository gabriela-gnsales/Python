# Tabuada v.3.0

while True:
    n = int(input('Informe o número para o cálculo da tabuada [para sair digite 0]: '))
    print('-' * 15)
    if n == 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i:<2} = {n * i}')
    print('-' * 15)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

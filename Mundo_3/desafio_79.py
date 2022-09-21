# Valores únicos em uma lista

print('=-' * 30)

lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('\033[0;32mValor adicionado com sucesso.\033[m')
    else:
        print('\033[0;31mValor duplicado! Não vou adicionar.\033[m')
    resp = input('Quer continuar [S/N]? ').strip().upper()[0]
    while resp != 'S' and resp != 'N':
        print('\033[0;31mOpção inválida! Responda novamente: \033[m')
        resp = input('Quer continuar [S/N]? ').strip().upper()[0]
    # if resp == 'N':
    if resp in 'N':
        break
print('=-' * 30)
print('Você digitou os valores:', lista)
print('Lista ordenada em ordem crescente:', sorted(lista))
print('Você digitou os valores:', lista)
lista.sort()
print('Lista ordenada em ordem crescente:', lista)

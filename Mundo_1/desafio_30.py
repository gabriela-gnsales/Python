# Par ou ímpar

n = int(input('Informe um número: '))

cores = {'limpa': '\033[m', 'vermelho': '\033[1;31;40m'}

if n % 2 == 0:
    print(f'O número {cores["vermelho"]}{n}{cores["limpa"]} é PAR.')
else:
    print('O número {}{}{} é ÍMPAR.'.format('\033[1;36;40m', n, '\033[m'))

salario = float(input('Digite o salário: R$ '))
aumento = float(input('Digite o valor percentual do aumento do salário: '))

novoSalario = salario * (1 + (aumento / 100))

print('O novo salário com o aumento será R$ {:.2f}.'.format(novoSalario))

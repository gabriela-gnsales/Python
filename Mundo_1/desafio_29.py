# Radar eletrônico

velocidade = float(input('Informe a velocidade do carro em km/h: '))

if velocidade > 80:
    print('\033[1;31;40mMULTADO! Você excedeu o limite permitido que é de 80 km/h.\033[m')
    multa = (velocidade - 80) * 7
    print(f'O valor da multa é de R$ {multa:.2f}.')
else:
    print('\033[4;30;42mA velocidade está dentro do valor permitido.\033[m')

# Pintando parede

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))

area = l * a
qtd_tinta = area / 2

print('A área da parede a ser pintada é {:.1f} metros e a quantidade de tinta necessária é {:.1f} litros.'.format(area, qtd_tinta))

# Conversor de medidas

n = float(input('Digite um valor em metros: '))

cm = n * 100
mm = n * 1000

print('O valor de {:.1f} m é igual a {:.1f} cm e igual a {:.1f} mm.'.format(n, cm, mm))

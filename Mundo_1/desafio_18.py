# Seno, cosseno e tangente

from math import radians, sin, cos, tan

ang = radians(float(input('Digite o valor de um ângulo em graus: ')))

print('O seno desse ângulo é {:.1f}.\nO cosseno é {:.1f}.\nA tangente é {:.1f}'.format(sin(ang), cos(ang), tan(ang)))

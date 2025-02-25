# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro da tinta pinta uma área de 2m².

# usando a váriavel para largura e altura, f-string e o cálculo feito dentro do prórpio print
'''larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

print(f'A parede com {larg} x {alt}, tem área {larg * alt:.2f}m² e é necessário {(larg * alt) / 2:.2f} litros de tinta para pintá-la.')
'''

# declarei as variáveis por fora e usei o .format()
'''l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l * a
tinta = area / 2

print('A parede com {:.1f} x {:.1f}, tem área: {:.1f}m² e é necessário {}l de tinta para pintá-la.' .format(l, a, area, tinta))
'''

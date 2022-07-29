# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))
area = larg * alt
print('Sua parede tem a dimensão de {}mx{}m.'.format(larg, alt))
print('Portanto, sua área é de {}m².'.format(area))
tinta = area/2
print('Para pintar essa parede, são necessários {:.2f}l de tinta.'.format(tinta))

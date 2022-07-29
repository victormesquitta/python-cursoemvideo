# Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('Para o ângulo de {:.2f}º:'.format(angulo))
print('O seno é de {:.2f}.'.format(sen))
print('O cosseno é de {:.2f}.'.format(cos))
print('A tangente é de {:.2f}.'.format(tan))

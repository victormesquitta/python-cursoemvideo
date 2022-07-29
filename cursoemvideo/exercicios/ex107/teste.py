# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
# e use algumas dessas funções.

import moeda

preco = float(input("Digite um preço: R$"))
print(f'A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}.'
      f'\nO dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}.'
      f'\nAumentando 10%, temos {moeda.aumentar(preco, 10):.2f}.'
      f'\nDiminuindo 10%, temos {moeda.diminuir(preco, 10):.2f}.')

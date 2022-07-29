# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

import moeda

preco = float(input("Digite um preço: R$"))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}.'
      f'\nO dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}.'
      f'\nAumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}.'
      f'\nDiminuindo 10%, temos {moeda.moeda(moeda.diminuir(preco, 10))}.')

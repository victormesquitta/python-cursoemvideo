# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$'))
desco = preco * 0.95
print('O produto que custava R${},'.format(preco), end=' ')
print('na promoção, com desconto de 5% vai custar R${}.'.format(desco))

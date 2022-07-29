#   Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#   e mostre quantos dólares, euros e libras ela pode comprar
#   (considerando [US1,00 = R$5.20] //  [1,00 € = R$6,13] // [£1,00 = R$7,23] – 11/08/2021).

reais = float(input('Quanto reais você tem na carteira? R$ '))
dolar = reais/5.22
euro = reais/6.13
libra = reais/7.23
print('Com R${:.2f} você pode comprar:\nUS${:.2f}.'.format(reais, dolar))
print('€{:.2f}.'.format(euro))
print('£${:.2f}.'.format(libra))

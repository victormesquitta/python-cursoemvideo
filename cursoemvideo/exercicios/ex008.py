# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite uma distância em metros: '))
print('{}km'.format(n/1000))
print('{}hm'.format(n/100))
print('{}dam'.format(n/10))
print('{}dm'.format(n*10))
print('{}cm'.format(n*100))
print('{}mm'.format(n*1000))

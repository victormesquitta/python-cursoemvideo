# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar a viagem de {:.2f}Km.'.format(dist))
if dist <= 200:
    valor = dist * 0.5
else:
    valor = dist * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(valor))

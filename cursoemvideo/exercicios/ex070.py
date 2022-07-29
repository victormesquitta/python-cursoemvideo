# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

gastoTOTAL = prod1000 = menor = nomeBARATO = 0
print('''--------------------------------
      LOJAS SUPER BARATÃO      
--------------------------------''')
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    gastoTOTAL += preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    if preco > 1000:
        prod1000 += 1
    if menor == 0:
        menor = preco
        nomeBARATO = produto
    if menor > preco:
        menor = preco
        nomeBARATO = produto
print('-------- FIM DO PROGRAMA --------')
print('''O total da compra foi R${:.2f}
Temos {} produtos custando mais de R$1000.00
O produto mais barato foi um(a) {} que custa R${:.2f}'''.format(gastoTOTAL, prod1000, nomeBARATO, menor,))

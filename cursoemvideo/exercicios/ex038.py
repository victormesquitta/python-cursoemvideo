# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem.

n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n1 < n2:
    print('O SEGUNDO valor é maior.')
elif n1 == n2:
    print('Os dois números são IGUAIS.')

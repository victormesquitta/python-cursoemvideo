# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = soma = contador = 0
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    soma += n
    contador += 1
print('Você digitou {} números e a soma entre eles resultou em {}.'.format(contador - 1, soma - 999))

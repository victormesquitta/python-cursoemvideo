# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

cont = 0
soma = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos {} valores pares digitados foi de {}'.format(cont, soma))

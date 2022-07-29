# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Me diga um numero qualquer: '))
if (num % 2) > 0:
    print('O número {} é ÍMPAR.'.format(num))
else:
    print('O número {} é PAR.'.format(num))

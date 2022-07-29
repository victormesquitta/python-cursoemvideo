# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 20)
print('10 TERMOS DE UMA P.A.')
print('=' * 20)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(n1, n1 + (razao * 10), razao):
    print('{} > '.format(c), end='')
print('ACABOU', end='')

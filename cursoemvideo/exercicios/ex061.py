# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
print('-=' * 15)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 0
while contador != 10:
    print('{} > '.format(n1), end='')
    n1 += razao
    contador += 1
print('FIM', end='')

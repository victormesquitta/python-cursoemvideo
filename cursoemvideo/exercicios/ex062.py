# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
print('-=' * 15)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = n1
contador = 1
total = 0
maistermos = 10
while maistermos != 0:
    total += maistermos
    while contador <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    maistermos = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos exibidos'.format(total))

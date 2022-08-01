# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

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

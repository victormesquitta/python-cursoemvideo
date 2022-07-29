# Crie um programa que faça o computador jogar Jokenpô com você.

import time
from random import randint
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ')
computador = randint(0, 2)
print('-=' * 12)
print('''Computador jogou {}
Jogador jogou {}'''.format(itens[computador], itens[jogada]))
print('-=' * 12)
if computador == 0:  # SE O COMPUTADOR JOGAR PEDRA
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('JOGADOR VENCEU')
    elif jogada == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:  # SE O COMPUTADOR JOGAR PAPEL
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  # SE O COMPUTADOR JOGAR TESOURA
    if jogada == 0:
        print('JOGADOR VENCEU')
    elif jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

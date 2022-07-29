# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
             'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print("Valores sorteados: ")
for k, v in jogadas.items():
    print(f"O {k} tirou {v} no dado.")
    sleep(1)
print("-=" * 20)
print("  == RANKING DOS JOGADORES ==  ")
ranking = []
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for pos, v in enumerate(ranking):
    print(f"   {pos+1}° lugar: {v[0]} com {v[1]}.")
    sleep(1)

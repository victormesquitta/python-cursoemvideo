# Escreva um programa que faça o computador “pensar” em um número inteiro entre 1 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tenta adivinhar...')
print('-=-'*20)
numero = int(input('Em que número pensei? ')) # Jogador tenta adivinhar.
computador = random.randint(1, 5) # Randomiza o numero que o computador irá pensar.
print('PROCESSANDO...')
time.sleep(3) #Sleep faz o resto do código aparecer depois de tantos segundos.
if random != numero: # != é o símbolo de diferente na matemática.
    print('PERDEU! Eu pensei no número {} e não no número {}!'.format(computador, numero))
else:
    print('GANHOU! Você conseguiu me vencer')

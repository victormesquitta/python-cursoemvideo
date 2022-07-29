# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')
jogador = int(input('Qual é o seu palpite? '))
computador = randint(0, 10)
palpites = 1
while jogador != computador:
    if jogador < computador:
        jogador = int(input('Mais... Tente mais uma vez.\nQual é o seu palpite? '))
        palpites += 1
    elif jogador > computador:
        jogador = int(input('Menos... Tente mais uma vez.\nQual é o seu palpite? '))
        palpites += 1
if palpites < 2:  # Só para começar a fazer diferenciação de plural nas strings
    print("Acertou com {} tentativa. Parabéns!".format(palpites))
else:
    print("Acertou com {} tentativas. Parabéns!".format(palpites))

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
numeros = []
listadejogos = []
print("=" * 30 + "\n" + "JOGA NA MEGA SENA".center(30, " ") + "\n" + "=" * 30 + "\n")
jogos = int(input("Quantos jogos você quer que eu sorteie? "))
print()
print("-=" * 3 + f" SORTEANDO {jogos} JOGOS " + "-=" * 3)
for sorteadordejogos in range(0, jogos):
    for sorteadordenumeros in range(0, 6):
        while True:
            x = randint(1, 60)
            if x not in numeros:
                numeros.append(x)
                break
    numeros.sort()
    listadejogos.append(numeros[:])
    print(f"JOGO {sorteadordejogos + 1}:" + f"{listadejogos[sorteadordejogos]}")
    numeros.clear()
print()
print("-=" * 5 + " < BOA SORTE! > " + "-=" * 5)

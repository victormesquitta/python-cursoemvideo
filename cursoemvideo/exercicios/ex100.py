# Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from time import sleep
from random import randint


def sorteia():
    print('Sorteando os valores da lista: ', end='')
    sleep(1)
    for c in range(0, 5):
        num.append(randint(0, 9))
        print(num[c], end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar():
    somador = 0
    for valor in num:
        if valor % 2 == 0:
            somador += valor
    print(f'Somando os valores pares de {num}, temos {somador}.')


num = []
sorteia()
somaPar()

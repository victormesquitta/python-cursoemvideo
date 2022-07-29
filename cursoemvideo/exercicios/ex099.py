# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*x):
    cont = maior = 0
    print("=-" * 20)
    print(f'Analisando os valores passados...')
    sleep(1)
    for c in x:
        if cont == 0:
            maior = cont
        elif c > maior:
            maior = c
        print(c, end=' ')
        cont += 1
        sleep(0.5)
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#  Programa Principal
maior(0, 7, 9, 3)
maior(2, 1, 3)
maior(9, 6, 4, 0)
maior()

# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1;
#  b) de 10 até 0, de 2 em 2;
# c) uma contagem personalizada.

import time


def contagem(start, stop, step):
    print('=-' * 20)
    print(f'Contagem de {start} até {stop-1} de {step} em {step}:')
    time.sleep(2)
    for c in range(start, stop, step):
        time.sleep(0.3)
        print(c, end=' ')
    time.sleep(0.3)
    print("FIM!")


contagem(1, 11, 1)
contagem(10, 0, -2)
print('=-' * 20)
print('Agora é sua vez de personalizar a contamgem: ')
inicio = int(input("Início: "))
fim = int(input("Fim:    "))
passo = int(input("Passo:  "))
contagem(inicio, fim, passo)

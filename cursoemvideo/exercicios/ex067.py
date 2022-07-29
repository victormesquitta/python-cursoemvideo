# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

n = 0
while True:
    n = int(input('''================================
Quer ver a tabuada de qual valor? '''))
    print('================================')
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    if n < 0:
        print('''=========================================
PROGRAMA TABUADA ENCERRADO. Volte sempre!
=========================================''')
        break

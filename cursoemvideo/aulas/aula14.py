'''for c in range(1, 10):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''

'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')'''

#  Enquanto o número (n) for diferente de 0, ele continuará rodando o algoritmo
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares'.format(par, impar))

# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar;
# [ 2 ] multiplicar;
# [ 3 ] maior;
# [ 4 ] novos números;
# [ 5 ] sair do programa.

from time import sleep
opcao = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
        print('-=='*8)
        sleep(3)
    elif opcao == 2:
        print('O resultado de {} X {} é {}'.format(n1, n2, n1 * n2))
        print('-=='*8)
        sleep(3)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        print('-==' * 8)
        sleep(3)
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(5)
        print('Fim do programa! Volte sempre!')
        print('-==' * 8)
    else:
        print('Opção inválida. Tente novamente')
        print('-==' * 8)
        sleep(3)

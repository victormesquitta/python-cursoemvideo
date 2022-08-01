# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = continuacao = contador = soma = 0
maior = menor = 0
while continuacao != 'N':
    n = int(input('Digite um número: '))
    contador += 1
    soma += n
    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuacao = str(input('Quer continuar [S/N]? ')).strip().upper()
    while continuacao not in 'SN':
        continuacao = str(input('Opção inválida. Quer continuar [S/N]? ')).strip().upper()
media = soma / contador
print('Você digitou {} números e a média entre eles resultou em {:.2f}'.format(contador, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))

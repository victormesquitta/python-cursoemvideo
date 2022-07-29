# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# Desafio extra: Fazer ele rodar até o usuário dizer que não utilizará mais.

numextenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
              'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
              'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    while escolha < 0 or escolha > 20:
        escolha = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numextenso[escolha]}')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

total = NCinquenta = NVinte = NDez = NUm = 0
print('=' * 30)
print('          BANCO CEV          ')
print('=' * 30)
saque = float(input('Que valor você quer sacar? R$'))
if saque // 50 > 0:
    NCinquenta = saque // 50
    total = saque - (NCinquenta * 50)
    print(f'Total de {NCinquenta:.0f} cédulas de R$50')
if saque // 20 > 0:
    NVinte = total // 20
    total += -NVinte * 20
    print(f'Total de {NVinte:.0f} cédulas de R$20')
if saque // 10 > 0:
    NDez = total // 10
    total += -NDez * 10
    print(f'Total de {NDez:.0f} cédulas de R$10')
if saque // 1 > 0:
    NUm = total // 1
    print(f'Total de {NUm:.0f} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

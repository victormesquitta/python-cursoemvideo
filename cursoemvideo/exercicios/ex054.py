# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
contmenor = 0
contmaior = 0
for datas in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(datas)))
    if atual - ano < 18:
        contmenor += 1
    else:
        contmaior += 1
print('''Ao todo tivemos {} pessoas menores de idade
E também tivemos {} pessoas maiores de idade'''.format(contmenor, contmaior))

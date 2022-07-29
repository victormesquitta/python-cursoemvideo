# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Ano de nascimento: '))
idade = 2021 - ano
atual = date.today().year
print('Quem nasceu em {} tem {} anos em 2021'.format(ano, idade))
if idade < 18:
    tempo = 18 - idade
    alistamento = date.today().year + tempo
    print('''Ainda falta {} ano(s) para o alistamento
Seu alistamento será em {}.'''.format(tempo, alistamento))
elif idade > 18:
    tempo = idade - 18
    alistamento = date.today().year - tempo
    print('''Você já deveria ter se alistado a {} ano(s)
Seu alistamento foi em {}.'''.format(tempo, alistamento))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')

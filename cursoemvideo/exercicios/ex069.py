# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

tot18 = totH = totM20 = 0
print('-' * 25)
print('  CADASTRE UMA PESSOA  ')
print('-' * 25)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 20)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if idade < 20 and sexo == 'F':
        totM20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('-' * 25)
print(f'''Total de pessoas com mais de 18 anos: {tot18}.
Ao todo temos {totH} homens cadastrados.
E temos {totM20} mulheres com menos de 20 anos.''')

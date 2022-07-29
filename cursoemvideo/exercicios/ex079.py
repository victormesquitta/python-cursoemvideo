# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

listanum = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in listanum:
        listanum.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar [S/N] ? ')).strip().upper()
    while continuar[0] not in 'SN':
        continuar = str(input('Resposta Inválida. Você quer continuar [S/N] ? ')).strip().upper()
    if continuar[0] in 'N':
        break
print('-='*20)
listanum.sort()
print(f'Você digitou os valores {listanum}')

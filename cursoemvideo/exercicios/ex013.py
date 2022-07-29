# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario+(salario * (15/100))
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, '.format(salario), end='')
print('passa a receber R${:.2f}.'.format(aumento))

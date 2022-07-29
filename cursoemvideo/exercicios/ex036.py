# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Valor da casa: R$'))
salario = float(input('Sálario do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
parcela = valor / (tempo * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, tempo, parcela))
if parcela > (salario * 0.3):
    print('\033[1;31mEMPRÉSTIMO NEGADO\033[m')
else:
    print('\033[1;32mEMPRÉSTIMO AUTORIZADO\033[m')

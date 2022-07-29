# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – À vista dinheiro/cheque: 10% de desconto;
# – À vista no cartão: 5% de desconto;
# – Em até 2x no cartão: preço formal;
# – 3x ou mais no cartão: 20% de juros.

print('{} LOJAS MESQUITA {}'.format('=' * 10, '=' * 10))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco * 0.9))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco * 0.95))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(preco / 2))
    print('Sua compra vai custar R${:.2f} no final.'.format(preco))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, (preco / parcelas) * 1.2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco * 1.2))
else:
    print('OPÇÃO INVÁLIDA, tente novamente!')

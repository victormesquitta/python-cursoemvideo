# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
ctps = {'nome': str(input('Nome: ')), 'idade': datetime.now().year - int(input('Ano de nascimento: ')),
        'carteira': int(input('Carteira de Trabalho (0 = não tem): '))}
if ctps['carteira'] != 0:
    ctps['contratação'] = int(input("Ano de contratação: "))
    ctps['salário'] = float(input("Salário: R$"))
    ctps['aposentadoria'] = ctps['contratação'] - (datetime.now().year - ctps['idade']) + 35
print("=-" * 20)
for k, v in ctps.items():
    print(f"{k} tem o valor {v}.")

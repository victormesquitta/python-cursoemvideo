# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘).

def leiaInt(msg):
    while True:
        valor = str(input(msg)).strip()
        if valor.isnumeric():
            valor = int(valor)
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
    return valor


#  PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o numero {n}.')

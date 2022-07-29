# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista1 = []
listapar = []
listaimpar = []

while True:
    valor = int(input("Digite um valor: "))
    lista1.append(valor)
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    continuacao = str(input("Deseja continuar [S/N] ? ")).strip().upper()
    if "N" in continuacao:
        break
print("=-" * 30)
print(f"A lista completa ficou {lista1}")
print(f"A lista de pares é {listapar}")
print(f"A lista de ímpares é {listaimpar}")

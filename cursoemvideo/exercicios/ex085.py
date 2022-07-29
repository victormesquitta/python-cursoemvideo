# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

listadenumeros = [[], []]
for c in range(1, 8):
    n = int(input(f"Digite o {c}º valor: "))
    if n % 2 == 0:
        listadenumeros[0].append(n)
    else:
        listadenumeros[1].append(n)
listadenumeros[0].sort()
listadenumeros[1].sort()
print("=-" * 30)
print(f"Os valores pares digitados foram: {listadenumeros[0]}")
print(f"Os valores ímpares digitados foram: {listadenumeros[1]}")

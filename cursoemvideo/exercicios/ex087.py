# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna3 = maiorlinha2 = 0
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[linha])):
        matriz[linha][coluna] = int(input(f"Digite um número para [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
        if coluna == 2:
            somacoluna3 += matriz[linha][coluna]
        if linha == 1 and coluna == 0:
            maiorlinha2 = matriz[linha][coluna]
        elif linha == 1 and coluna > 0:
            if matriz[linha][coluna] > maiorlinha2:
                maiorlinha2 = matriz[linha][coluna]
print("=-" * 30)
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[linha])):
        print(f"[{matriz[linha][coluna]:^5}]", end='')
    print()
print("=-" * 30)
print("A soma de todos os valores pares digitados foi ", somapar)
print("A soma dos valores da terceira coluna foi ", somacoluna3)
print("O maior valor da segunda linha foi ", maiorlinha2)

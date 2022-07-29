# Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
# com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[0])):
        matriz[linha][coluna] = int(input("Digite um número para [{0}, {1}]: ".format(linha, coluna)))
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[0])):
        print(f"[{matriz[linha][coluna]:^5}]", end='')
    print()

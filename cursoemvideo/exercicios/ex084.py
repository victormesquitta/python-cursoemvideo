# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# •	Quantas pessoas foram cadastradas.
# •	Uma listagem com as pessoas mais pesadas.
# •	Uma listagem com as pessoas mais leves.

pessoaatual = []
grupo = []
pesadas = leves = 0
while True:
    pessoaatual.append(str(input("Nome: ")))
    pessoaatual.append(float(input("Peso [em kg]: ")))
    if len(grupo) == 0:
        pesadas = leves = pessoaatual[1]
    else:
        if pessoaatual[1] > pesadas:
            pesadas = pessoaatual[1]
        if pessoaatual[1] < leves:
            leves = pessoaatual[1]
    grupo.append(pessoaatual[:])
    pessoaatual.clear()
    continuacao = str(input("Quer continuar [S/N] ? ")).strip().upper()
    if "N" in continuacao:
        break

print("=-" * 30)
print(f"Ao todo, você cadastrou {len(grupo)} pessoas.")
print(f"O maior peso foi de {pesadas}kg. Peso de ", end='')
for p in grupo:
    if p[1] == pesadas:
        print(f"[{p[0]}]", end='')
print()
print(f"O menor peso foi de {leves}kg. Peso de: ", end='')
for p in grupo:
    if p[1] == leves:
        print(f"[{p[0]}]", end="")

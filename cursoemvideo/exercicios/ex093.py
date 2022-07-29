# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

contagemdegols = {'jogador': str(input("Nome do jogador: "))}
partidas = int(input(f"Quantas partidas {contagemdegols['jogador']} jogou? "))
golspartida = []
for c in range(0, partidas):
    golspartida.append(int(input(f'     Quantos gols na partida {c}? ')))
contagemdegols['gols'] = golspartida[:]
contagemdegols['total'] = sum(golspartida)  # sum: soma tudo que estiver dentro da lista
print("=-" * 20)
print(contagemdegols)
print("=-" * 20)
for k, v in contagemdegols.items():
    print(f"O campo {k} tem valor {v}.")
print("=-" * 20)
print(f"O jogador {contagemdegols['jogador']} jogou {len(contagemdegols['gols'])} partidas.")
for i, v in enumerate(contagemdegols['gols']):
    print(f"    => Na partida {i}, fez {v} gols,")
print(f"Fez um total de {contagemdegols['total']} gols.")

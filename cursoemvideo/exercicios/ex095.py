# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

listadejogadores = []
contagemdegols = dict()
while True:
    contagemdegols.clear()
    contagemdegols = {'jogador': str(input("Nome do jogador: "))}
    partidas = int(input(f"Quantas partidas {contagemdegols['jogador']} jogou? "))
    golsnaspartidas = []
    for c in range(0, partidas):
        golsnaspartidas.append(int(input(f'     Quantos gols na partida {c}? ')))
    contagemdegols['gols'] = golsnaspartidas[:]
    contagemdegols['total'] = sum(golsnaspartidas)  # sum: soma tudo que estiver dentro da lista
    listadejogadores.append(contagemdegols.copy())
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if continuar in "SN":
            break
        print("RESPOSTA INVÁLIDA! Tente novamente.")
    if continuar == "N":
        break
print('=-' * 20)
print('cod ', end='')
for i in contagemdegols.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(listadejogadores):
    print(f'{k}'.rjust(3), end=' ')
    for d in v.values():
        print(f'{d}'.ljust(15), end='')
    print()
while True:
    print('-' * 40)
    dados = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if dados == 999:
        print('<< VOLTE SEMPRE >>')
        break
    if len(listadejogadores)-1 < dados or dados < 0:
        print("NENHUM JOGADOR POSSUI ESSE CÓDIGO. Tente outro número.")
    else:
        print(f' == LEVANTAMENTO DO JOGADOR {listadejogadores[dados]["jogador"]}:')
        for i, v in enumerate(listadejogadores[dados]['gols']):
            print(f'    No jogo {i+1} fez {v} gols.')

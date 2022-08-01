# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará SC', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('-='*15)
print('Lista de times do Brasileirão:', times)
print('-='*15)
print('Os 5 primeiros times são:', times[0:5])
print('-='*15)
print('Os 4 últimos são:', times[-4:])
print('-='*15)
print('Times em ordem alfabética:', sorted(times))
print('-='*15)
for pos, time in enumerate(times):
    if time == 'Chapecoense':
        print(f'O Chapecoense está na {pos + 1}º posição.')

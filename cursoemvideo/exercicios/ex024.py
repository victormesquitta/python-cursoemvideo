# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Em que cidade você? ')).strip()
print(cid[:3].upper() == 'RIO')

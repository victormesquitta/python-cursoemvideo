# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) A média de idade;
# C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média.

pessoa = dict()
listadecadastro = list()
somaidade = 0
while True:
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if pessoa['sexo'] in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    somaidade += pessoa['idade']
    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
        if continuar in "SN":
            break
        print("ERRO! Responda com S ou N.")
    listadecadastro.append(pessoa.copy())
    if continuar == "N":
        break
mediaidade = somaidade / len(listadecadastro)
print("=-" * 20)
print(f"A) Ao todo temos {len(listadecadastro)} pessoas cadastradas.")
print(f"B) A média de idade é de {mediaidade:5.2f} anos.")
print("C) As mulheres cadastradas foram", end=' ')
for p in listadecadastro:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print("\nD) Lista das pessoas que estão acima da média:")
for p in listadecadastro:
    if p['idade'] > mediaidade:
        print('    ', end='')
        for k, v in p.items():
            print(f"{k} = {v};", end=' ')
        print()
print("<< ENCERRADO >>")

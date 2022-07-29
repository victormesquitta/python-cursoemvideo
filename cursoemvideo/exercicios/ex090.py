# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['média'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'NÃO APROVADO'
print("-=" * 20)
for k, v in aluno.items():
    print(f"- {k} é igual a {v}.")

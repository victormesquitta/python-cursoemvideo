# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

print()
print("=" * 20 + " GERANDO BOLETIM DOS ALUNOS " + "=" * 20)
sala = []
aluno = []
contadordealunos = 0
while True:
    aluno.append(str(input("Nome do aluno: ")).strip())
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    sala.append(aluno[:])
    aluno.clear()
    contadordealunos += 1
    continuacao = str(input("Quer continuar [S/N]? ")).upper().strip()
    if "N" in continuacao:
        break
print("-=" * 13)
print(f"{'No.':<5}{'NOME':<11}{'MÉDIA'}")
print("-" * 26)
for aluno in range(0, contadordealunos):
    media = (sala[aluno][1] + sala[aluno][2]) / 2
    print(f"{aluno:<5}" + f"{sala[aluno][0]:<15}" + f"{media}")
while True:
    print("-" * 40)
    consultanota = int(input("Mostrar notas de qual aluno (999 interrompe) ? "))
    if consultanota == 999:
        break
    print(f"As notas de {sala[consultanota][0]} foram {sala[consultanota][1]} e {sala[consultanota][2]}.")
print("Finalizando...\n    <<<= VOLTE SEMPRE =>>>")

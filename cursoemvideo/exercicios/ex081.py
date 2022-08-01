# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# •	Quantos números foram digitados.
# •	A lista de valores, ordenada de forma decrescente.
# •	Se o valor 5 foi digitado e está ou não na lista.

lista = []
contador = 0
while True:
    lista.append(int(input("Digite um valor: ")))
    continuacao = str(input("Quer continuar [S/N]? ")).strip().upper()
    contador += 1
    if 'N' in continuacao[0]:
        break
lista.sort(reverse=True)
print(f"{contador} elementos foram digitados.")
print(f"Os valores em ordem decrescente são: {lista}")
if 5 in lista:
    print("O número 5 ESTÁ na lista.")
else:
    print("O número 5 NÃO está na lista.")

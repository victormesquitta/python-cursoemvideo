# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.

contadordeparentesesaberto = 0
contadordeparentesesfechado = 0
expressao = str(input("Digite uma expressão: "))
for i, p in enumerate(expressao):
    if p == "(":
        contadordeparentesesaberto += 1
    elif p == ")":
        contadordeparentesesfechado += 1
    if contadordeparentesesfechado > contadordeparentesesaberto:
        break
if contadordeparentesesaberto == contadordeparentesesfechado:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está incorreta!")

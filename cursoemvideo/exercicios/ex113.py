# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mERRO: por favor, digite um número INTEIRO válido.\033[m")
        except (KeyboardInterrupt):
            print("\033[1;31mO usuário preferiu não digitar esse número.\033[m")
            break
        else:
            return i


def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mERRO: por favor, digite um número REAL válido.\033[m")
        except (KeyboardInterrupt):
            print("\033[1;31mO usuário preferiu não digitar esse número.\033[m")
            break
        else:
            return r


#  Programa principal
int = leiaInt("Digite um número Inteiro: ")
real = leiaFloat("Digite um número Real: ")
print(f"O numero inteiro digitado foi {int} e o real foi {real}.")

def leiaInt(msg):
    while True:
        try:
            resp = int(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mERRO: por favor, digite um número INTEIRO válido.\033[m")
        except (KeyboardInterrupt):
            print("\033[1;31mO usuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return resp

def linha(tam=40):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for pos, opcao in enumerate(lista):
        print(f'\033[1;33m{pos+1}\033[m - \033[1;34m{opcao}\033[m')
    print(linha())
    opc = leiaInt('\033[1;32mSua opção:\033[m ')
    return opc

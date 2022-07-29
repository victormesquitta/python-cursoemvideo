def aumentar(dinheiro=0, taxa=0, formatacao=False):
    res = dinheiro + (dinheiro * taxa / 100)
    return moeda(res)


def diminuir(dinheiro=0, taxa=0, formatacao=False):
    res = dinheiro - (dinheiro * taxa / 100)
    return moeda(res)


def dobro(dinheiro=0, formatacao=False):
    res = dinheiro * 2
    return moeda(res)


def metade(dinheiro=0, formatacao=False):
    res = dinheiro / 2
    return moeda(res)


def moeda(dinheiro=0, moeda='R$'):
    return f'{moeda}{dinheiro:>.2f}'.replace('.', ',')


def resumo(dinheiro=0, aumento=0, reducao=0):
    print('-=' * 20)
    print('RESUMO DO VALOR'.center(40))
    print('-=' * 20)
    print(f'Preço analisado: \t{moeda(dinheiro)}')
    print(f'Dobro do preço: \t{dobro(dinheiro, True)}')
    print(f'Metade do preço: \t{metade(dinheiro, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(dinheiro, aumento, True)}')
    print(f'{reducao}% de aumento: \t{diminuir(dinheiro, reducao, True)}')
    print('-=' * 20)

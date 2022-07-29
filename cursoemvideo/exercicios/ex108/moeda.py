def aumentar(dinheiro=0, taxa=0):
    return dinheiro + (dinheiro * taxa / 100)


def diminuir(dinheiro=0, taxa=0):
    return dinheiro - (dinheiro * taxa / 100)


def dobro(dinheiro=0):
    return dinheiro * 2


def metade(dinheiro=0):
    return dinheiro / 2


def moeda(dinheiro=0, moeda='R$'):
    return f'{moeda}{dinheiro:8.2f}'.replace('.', ',')

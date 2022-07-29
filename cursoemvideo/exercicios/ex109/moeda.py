def aumentar(dinheiro=0, taxa=0, formatacao=False):
    res = dinheiro + (dinheiro * taxa / 100)
    return res if formatacao is False else moeda(res)


def diminuir(dinheiro=0, taxa=0, formatacao=False):
    res = dinheiro - (dinheiro * taxa / 100)
    return res if not formatacao else moeda(res)


def dobro(dinheiro=0, formatacao=False):
    res = dinheiro * 2
    return res if formatacao is False else moeda(res)


def metade(dinheiro=0, formatacao=False):
    res = dinheiro / 2
    return res if formatacao is False else moeda(res)


def moeda(dinheiro=0, moeda='R$'):
    return f'{moeda}{dinheiro:>.2f}'.replace('.', ',')

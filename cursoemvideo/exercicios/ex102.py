# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número:
    :param num: O número a ser calculado.
    :param show: Mostrar ou não o cálculo [opcional].
    :return: O valor do Fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
        f *= c
    return f


#  PROGRAMA PRINCIPAL
help(fatorial)
print(fatorial(5, show=True))

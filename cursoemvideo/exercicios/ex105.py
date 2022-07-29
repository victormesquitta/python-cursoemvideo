# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota;
# – A menor nota;
# – A média da turma;
# – A situação (opcional).                                                                                                                                                             – A média da turma;                                                                                                                                                      – A situação (opcional).

def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações obtidas de vários alunos:
    :param num: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a turma.
    """
    notasturma = dict()
    notasturma['total'] = len(num)
    notasturma['maior'] = max(num)
    notasturma['menor'] = min(num)
    notasturma['media'] = sum(num)/len(num)
    if sit:
        if notasturma['media'] < 5:
            notasturma['situção'] = 'RUIM'
        if 5 <= notasturma['media'] < 7.5:
            notasturma['situção'] = 'RAZOÁVEL'
        if 7.5 <= notasturma['media'] < 9:
            notasturma['situção'] = 'BOM'
        if 9 <= notasturma['media'] < 10:
            notasturma['situção'] = 'EXCEPCIONAL'
    return notasturma


#  PROGRAMA PRINCIPAL
print(notas(6, 7.5, 8, 10, 3.25, 5.75, sit=True))
help(notas)

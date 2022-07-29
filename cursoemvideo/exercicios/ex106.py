# Faça um minissistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.

c = ('\033[m',       # 0 - sem cor
     '\033[30;41m',  # 1 - vermelho
     '\033[42m',  # 2 - verde
     '\033[30;43m',  # 3 - amarelo
     '\033[30;44m',  # 4 - azul
     '\033[30;45m',  # 5 - roxo
     '\033[7;30m')   # 6 - branco


def ajuda(comando):
    titulo(f'Acessando o manual do comando {comando}', 4)
    print(c[5])
    help(comando)
    print(c[0], end='')


def titulo(msg, cor=0):
    print(c[cor])
    print('~' * (len(msg)+4))
    print(f'  {msg}')
    print('~' * (len(msg)+4))
    print(c[0], end='')

#  PROGRAMA PRINCIPAL
com = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    com = str(input('Função ou biblioteca > '))
    if com.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        ajuda(com)

# Vamos criar um menu em Python, usando modularização.

from cursoemvideo.exercicios.ex115c.lib.interface import *
from time import sleep


while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if opcao == 1:
        cabecalho(f'OPÇÃO {opcao}')
    elif opcao == 2:
        cabecalho(f'OPÇÃO {opcao}')
    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

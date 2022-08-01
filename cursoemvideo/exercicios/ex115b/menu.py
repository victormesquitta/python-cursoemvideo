# Vamos ver como fazer acesso a arquivos usando o Python.

from cursoemvideo.exercicios.ex115c.lib.interface import *
from cursoemvideo.exercicios.ex115c.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if opcao == 1:
        #  Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif opcao == 2:
        cabecalho(f'OPÇÃO {opcao}')
    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

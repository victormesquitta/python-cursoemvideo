# Vamos finalizar o projeto de acesso a arquivos em Python.

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
        cabecalho('NOVO CADASTRO')
        nome = str(input("Nome: "))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from cursoemvideo.exercicios.ex115a.lib.interface import *
from cursoemvideo.exercicios.ex115a.lib.arquivo import *
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

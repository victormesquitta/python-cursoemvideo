# Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função input(), mas com uma validação de dados
# para aceitar apenas valores que sejam monetários.

from cursoemvideo.exercicios.ex112.utilidadeCeV import moeda, dado

preco = dado.leiaDinheiro("Digite um preço: R$")
moeda.resumo(preco, 100, 30)

# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {}.'.format(n1, n2, media))
if media < 5:
    print('O aluno está \033[1;31mREPROVADO\033[m.')
elif 5.1 < media < 6.9:
    print('O aluno está em \033[1;33mRECUPERAÇÃO\033[m.')
elif media > 7:
    print('O aluno está \033[1;32mAPROVADO\033[m.')

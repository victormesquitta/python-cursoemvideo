nome = str(input('Qual é o seu nome? '))
if nome == 'Victor':
    print('Que nome \033[1;36mBONITO!\033[m')
elif nome == 'Pedro' or nome == 'Paulo' or nome == 'Maria':
    print('Seu nome é bastante \033[1;32mPOPULAR.\033[m')
elif nome in 'Elisabete Isabela Sabrina Fernanda':
    print('Belo nome \033[1;35mFEMININO\033[m é o seu.')
else:
    print('Seu nome é tão \033[1;31mNORMAL.\033[m')
print('Tenha um \033[1;33mBOM DIA\033[m, \033[1;4m{}!\033[m'.format(nome))

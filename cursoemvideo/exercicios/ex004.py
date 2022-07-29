#  Faça um programa que leia algo pelo teclado e
#  mostre na tela o seu tipo primitivo e todas as
#  suas informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())

from aulas.uteis import numeros  # As lib estão no arquivo uteis.py

n = int(input('Digite um valor: '))
fat = numeros.fatorial(n)
print(f'O fatorial de {n} é {fat}.')
print(f'O dobro de {n} é {numeros.dobro(n)}.')
print(f'o triplo de {n} é {numeros.triplo(n)}.')

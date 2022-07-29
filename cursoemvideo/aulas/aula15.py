n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += 999
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')  # fstrings: facilitam e substituem o .format

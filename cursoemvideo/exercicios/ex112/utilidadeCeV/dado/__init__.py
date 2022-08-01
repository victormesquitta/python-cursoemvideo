def leiaDinheiro(msg):
    while True:
        res = input(msg).strip().replace(',', '.')
        if res.isalpha() or res == '':
            print(f'\033[1;31mERRO! "{res}" é uma resposta inválida!\033[m')
        else:
            return float(res)

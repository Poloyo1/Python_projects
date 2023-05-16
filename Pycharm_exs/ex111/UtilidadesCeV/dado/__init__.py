def leiaDinheiro(a):
    ok = False
    valor = 0
    while not ok:
        n = str(input(a)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'Erro: \"{n}\" é um preço invalido')
        else:
            ok = True
            return float(n)

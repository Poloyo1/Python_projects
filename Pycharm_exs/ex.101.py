def voto(a):
    res = 2021 - a
    if res < 18:
        return print(f'Com {res} anos, Não Vota')
    if res > 18:
        if res > 65:
            return print(f'Com {res} anos, Voto Opicional')
        return print(f'Com {res} anos, Voto Obrigatorio ')


voto(a=int(input('Digite o seu ano de nascimento: ')))

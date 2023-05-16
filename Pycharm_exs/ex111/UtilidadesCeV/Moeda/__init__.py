def metade(a=0, moda=True):
    me = a / 2
    return me if moda is False else moeda(me)


def dobro(a=0, moda=True):
    do = a * 2
    return do if moda is False else moeda(do)


def aumentar(a=0, b=0, moda=True):
    con = (a * b) / 100
    au = a + con
    return au if moda is False else moeda(au)


def diminuir(a=0, b=0, moda=True):
    con = (a * b) / 100
    dim = a - con
    return dim if moda is False else moeda(dim)


def moeda(a=0, b='R$'):
    return f'{b}{a:.2f}'.replace('.', ',')


def resumo(a, c):
    print('=' * c)
    print('        RESUMO DO VALOR')
    print('-' * c)
    print(f'Preço analisado: {moeda(a):>15}')
    print(f'Dobro do preço:  {dobro(a):>15}')
    print(f'Metade do preço: {metade(a):>15}')
    print(f'10% de aumento:  {aumentar(a, 10):>15}')
    print(f'15% de redução:  {diminuir(a, 15):>15}')
    print('-' * c)

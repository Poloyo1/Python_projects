print('Calculador de Aréa')
print('=' * 40)


def area(a, b):
    ar = a * b
    print(f'A aréa de um terreno {a} X {b} é igual a {ar}m²')


area(a=float(input('Largura: ')), b=float(input('Comprimento: ')))

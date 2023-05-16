from time import sleep
print('=' * 40)


def contador(x, f, p):
    if x < f:
        print(f'Contegem de {x} até {f} de {p} em {p}:')
        for c in range(x, f + 1, p):
            print(f'{c} ', end='')
            sleep(0.4)
        print('Fim!')
    if x > f:
        if p < 0:
            p = p * -1
        if p == 0:
            p = 1
        print(f'Contagem regressiva de {x} até {f} de {p} em {p}: ')
        for c in range(x, f - p, -p):
            print(f'{c} ', end='')
            sleep(0.4)
        print('Fim!')


contador(1, 10, 1)
print('=' * 40)
contador(x=10, f=0, p=2)
print('=' * 40)
print('Agora é a sua vez de Pesonalizar a contagem!')
contador(x=int(input('Começo: ')), f=int(input('Fim: ')), p=int(input('casas a serem puladas: ')))
print('=' * 40)

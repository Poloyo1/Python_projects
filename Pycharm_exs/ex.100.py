from random import randint
from time import sleep
numeros = list()
pares = list()


def sorteio(lista):
    for c in range(0, 5):
        numeros.append(randint(1, 10))


def somaPar(listaa):
    soma = 0
    for x in listaa:
        soma += x
    print(f'A soma dos numeros pares de {numeros} é de {soma}')


print('Sorteando os valores: ', end='')
sorteio(numeros)
for r in numeros:
    if r % 2 == 0:
        pares.append(r)
for d in numeros:
    print(f'{d} ', end='')
    sleep(0.5)
print()
somaPar(pares)

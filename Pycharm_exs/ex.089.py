import random
from time import sleep
a = list()
b = list()
cont = 0
print('=' * 30)
print('     Sorteador de Jogos     ')
print('=' * 30)
n = int(input('Quantos jogos você quer que eu sorteie?: '))
for c in range(0, n):
    b.append(random.randint(0, 60))
    b.append(random.randint(0, 60))
    b.append(random.randint(0, 60))
    b.append(random.randint(0, 60))
    b.append(random.randint(0, 60))
    b.append(random.randint(0, 60))
    a.append(b[:])
    b.clear()
print('=' * 30)
print(f'Sorteando {n} jogos')
print('=' * 30)
for jo in a:
    cont += 1
    print(f'Jogo {cont}: {jo}')
    sleep(1)
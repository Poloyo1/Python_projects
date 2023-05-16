import random
from math import sqrt
import time
cont = 0
from operator import itemgetter
b = {'Jogador 1': random.randint(1, 6), 'Jogador 2': random.randint(1, 6), 'Jogador 3': random.randint(1, 6),
     'Jogador 4': random.randint(1, 6)}
ranking = dict()
print('=' * 40)
print('VALORES SORTEADOS')
print('=' * 40)
for k, v in b.items():
    print(f'O {k} tirou: {v} no dado')
    time.sleep(1)
print('=' * 40)
print('RANKING DOS JOGADORES')
print('=' * 40)
ranking = sorted(b.items(), key=itemgetter(1), reverse=True)
for k, v in ranking:
    cont += 1
    print(f'{cont}° lugar: {k} com {v} ')
    time.sleep(1)
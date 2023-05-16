from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os Numeros sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior numero sorteado foi {max(numeros)}')
print(f'O menor numero sorteado foi {min(numeros)}')

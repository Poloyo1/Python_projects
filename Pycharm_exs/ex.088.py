matriz = [[int(input('Digite um valor para a posição [0, 0]: ')),
           int(input('Digite um valor para a posição [0, 1]: ')),
           int(input('Digite um valor para a posição [0, 2]: '))],
          [int(input('Digite um valor para a posição [1, 0]: ')),
          int(input('Digite um valor para a posição [1, 1]: ')),
          int(input('Digite um valor para a posição [1, 2]: '))],
          [int(input('Digite um valor para a posição [2, 0]: ')),
           int(input('Digite um valor para a posição [2, 1]: ')),
           int(input('Digite um valor para a posição [2, 2]: '))]]
par = list()
soma = 0
somat = 0
for num in matriz:
    for x in num:
        if x % 2 == 0:
            par.append(x)
            soma = soma + x
for num in matriz[2]:
    somat = somat + num
print('=+' * 40)
print(f'A soma de todos os numeros pares da lista é igual a: {soma}')
print('=' * 80)
print(f'A soma de todos os numeros da terceira fileira é igual a: {somat}')
print('=' * 80)
print(f'O maior numero da segunda fileira foi: {max(matriz[1])}')
print('=+' * 40)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')
print('=+' * 40)
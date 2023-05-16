matriz = [[int(input('Digite um valor para a posição [0, 0]: ')),
           int(input('Digite um valor para a posição [0, 1]: ')),
           int(input('Digite um valor para a posição [0, 2]: '))],
          [int(input('Digite um valor para a posição [1, 0]: ')),
          int(input('Digite um valor para a posição [1, 1]: ')),
          int(input('Digite um valor para a posição [1, 2]: '))],
          [int(input('Digite um valor para a posição [2, 0]: ')),
           int(input('Digite um valor para a posição [2, 1]: ')),
           int(input('Digite um valor para a posição [2, 2]: '))]]
print('=' * 80)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')

from time import sleep


def maior(*num):
    print('=' * 60)
    print('Analisando os valores...')
    sleep(1)
    for x in num:
        print(f'{x} ', end='')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {max(num)}')


maior(4, 3, 2, 6, 9)
maior(6, 7, 2)
maior(0, 3)
maior(1)
maior(0)

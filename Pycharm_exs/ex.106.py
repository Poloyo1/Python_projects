from time import sleep
c = ['\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[0;30;46m',
     '\033[0;30;47m',
     '\033[7;30m']


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 5)
    sleep(0.5)
    print(c[8], end='')
    help(com)
    sleep(0.5)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PYHELP', 4)
    comando = str(input('função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)

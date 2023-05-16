while True:
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))
    print('\033[1m=======Menu=======')
    print('[1] soma')
    print('[2] multiplicação')
    print('[3] Qual o maior numero?')
    print('[4] Escolher outros numeros')
    print('[5] Sair do programa')
    print('==================')
    c = int(input('\033[m\033[0;32m>>Digite o numero correspondente ao o que você gostaria de fazer com esses numeros: '
                  '\033[m'))
    if c == 1:
        d = a + b
        print('Esse é o resultado da soma: {}'.format(d))
        break
    if c == 2:
        d = a * b
        print('Esse é o resultado da multiplicação: {}'.format(d))
        break
    if c == 3:
        if a < b:
            print('\033[0;34mO maior numero é {}\033[m'.format(b))
        elif a == b:
            print('\033[0;31mNenhum numero é maior os dois são iguais\033[m')
        if b < a:
            print('\033[0;34mO maior numero é {}\033[m'.format(a))
        break
    if c == 4:
        print('Prontinho!')
    if c == 5:
        break

print('\033[0;31mFim do programa!\033[m')
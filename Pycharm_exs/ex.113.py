def leiaint(nat):
    valor = 0
    while True:
        try:
            n = int(input(nat))
            valor = int(n)
            return valor
        except KeyboardInterrupt:
            print('\033[0;31mErro: O usuario prefiriu não digitar o valor!\033[m')
            valor = 0
            return valor
        except:
            print('\033[0;31mErro: por favor, digite um numero váldio\033[m')


def leiafloat(a):
    valor = 0
    while True:
        try:
            n = float(input(a).replace(',', '.'))
            valor = float(n)
            return valor
        except KeyboardInterrupt:
            print('\033[0;31mErro: O usuario prefiriu não digitar o valor!\033[m')
            valor = 0
            return valor
        except:
            print('\033[0;31mErro: por favor, digite um numero válido\033[m')


a = leiaint('Digite um numero inteiro: ')
b = leiafloat('Digite um numero real: ')
print(f'Você digitou um numero inteiro: {a} e um numero real: {b}'.replace('.', ','))

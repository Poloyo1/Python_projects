import random

def titulo(texto):
    print('\033[0;34m=\033[m' * 70)
    print(texto)
    print('\033[0;34m=\033[m' * 70)


def linha(linha):
    return print(f'\033[0;34m{linha}\033[m' * 70)


v = 0
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
na = random.choice(lista)
titulo('\033[1;35mJogo de Adivinhação!\033[m')
print('\033[0;36mO computador escolheu um numero, entre 0 e 20!\033[m')
print('\033[0;36mSerá que você consegue acertar qual foi?\033[m')
linha('-')
acertou = False
while True:
    esco = int(input('\033[0;36mDigite o numero que você acha que o computador escolheu:\033[m '))
    v += 1
    if esco == na:
        linha('=')
        print('\033[0;32mParabéns você acertou!\033[m')
        print(f'\033[0;36mVocê tentou {v} vezes\033[m')
        linha('=')
        break
    if v == 5:
        linha('=')
        print('\033[0;31mSuas chances acabaram. Fim de jogo!\033[m')
        print(f'\033[0;36mVocê tentou {v} vezes\033[m')
        print(f'\033[0;36mO Computador escolheu o numero:\033[m \033[0;31m{na}\033[m')
        linha('=')
        break
    else:
        if na < esco:
            print('\033[0;31mMenos, tente novamente.\033[m')
        elif na > esco:
            print('\033[0;35mMais, tente novamente.\033[m')

print('\033[0;31mFim\033[m')
linha('=')

from ex115 import pessoas
from ex115.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqexiste(arq):
    criararquivo(arq)

while True:
    try:
        pessoas.texto('Menu principal')
        print('\033[0;33m1 -\033[m \033[0;34mVer pessoas cadastradas\033[m')
        print('\033[0;33m2 -\033[m \033[0;34mCadastrar uma nova pessoa\033[m')
        print('\033[0;33m3 -\033[m \033[0;34mSair\033[m')
        print('-' * 50)
        a = int(input('\033[0;33mSua opção:\033[m '))
        if a == 1:
            pessoas.texto('Pessoas Cadastradas')
            lerarquivo(arq)
        elif a == 2:
            pessoas.texto('Novo Cadastro')
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            cadastrar(arq, nome, idade)
        elif a == 3:
            pessoas.texto('Saindo do Sistema... Até logo')
            break
        else:
            print('\033[0;31mErro: Digite uma opção valida\033[m')
            sleep(2)
    except:
        print('\033[0;31mErro: por favor, digite um numero inteiro valido\033[m')
        sleep(2)

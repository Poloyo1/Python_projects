from ex115 import pessoas


def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    a = open(nome, 'wt+')
    a.close()


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', ' ')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        a.close()


def cadastrar(arqn, nome='DESCONHECIDO', idade=0):
    try:
        a = open(arqn, 'at')
    except:
        print('Erro')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro')
        else:
            print(f'Registro de {nome}, realizado com sucesso')


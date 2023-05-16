def leiaint(nat):
    ok = False
    valor = 0
    while True:
        n = str(input(nat))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro digite um numero inteiro valido')
        if ok:
            break
    return valor


#Programa principal
n = leiaint('Digite um numero: ')
print(f'Você digitou o numero {n}')
a = []
while True:
    b = int(input('Digite um valor: '))
    if b not in a:
        a.append(b)
        print('Numero adicionado com sucesso')
        print('=' * 30)
    else:
        print('Numero repetido,portanto não irei considerar!')
        print('=' * 30)
    c = str(input('Gostaria de continuar?[S/N]: ')).upper()
    print('=' * 30)
    if c in 'N':
        print('ok...')
        break
a.sort()
print('=' * 30)
print(f'Essa é a lista em ordem crescente: {a}')
print('=' * 30)
print('fim')

a = []
while True:
    a.append(int(input('Digite um valor: ')))
    print('-' * 80)
    b = str(input('Gostaria de continuar?[S/N]: ')).upper()
    if b in 'N':
        break
    elif b != 'S' and 'N':
        print('-' * 80)
        c = str(input('Erro na resposta tente novamente![S/N]: ')).upper()
        print('-' * 80)
print('=' * 80)
print(f'Existem {len(a)} numeros na lista.')
print('=' * 80)
a.sort(reverse=True)
print(f'Essa é a lista em ordem decrescente: {a}')
print('=' * 80)
if 5 in a:
    print('O numero 5 está na lista')
    print('=' * 80)
else:
    print('O numero 5 não faz parte da lista')
    print('=' * 80)

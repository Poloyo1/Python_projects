a = int(input('Digite um numero: '))
c = a
f = 1
print('Calculando {}! = '.format(a), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

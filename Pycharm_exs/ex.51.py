a = int(input('Digite o primeiro termo: '))
b = int(input('Digite a razão: '))
c = a + (10 - 1) * b
for c in range(a, c + b, b):
    print('{}' .format(c), end=' == ')
print('Acabou!')

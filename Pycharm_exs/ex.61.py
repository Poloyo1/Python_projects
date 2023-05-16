a = int(input('Digite o primeiro termo: '))
b = int(input('Digite a razão: '))
c = 1
t = a
while c <= 10:
    print('{} -> '.format(t), end='')
    t += b
    c += 1
print('Fim')
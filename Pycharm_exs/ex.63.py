a = int(input('Digite um numero qualquer: '))
print('Mostrarei agora {} termos da sequencia de Fiboonati!')
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= a:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' -> Fim')

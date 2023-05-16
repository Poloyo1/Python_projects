a = int(input('Digite o primeiro termo: '))
b = int(input('Digite a razão: '))
c = 1
t = a
to = 0
m = 10
while m != 0:
    to = to + m
    while c <= to:
        print('{} -> '.format(t), end='')
        t += b
        c += 1
    print('Pausa!')
    m = int(input('Quantos termos você quer mostrar a mais? '))
print('Isse foi o total {}'.format(to))
print('Fim')

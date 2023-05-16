r = 'S'
s = m = q = ma = me = 0
while r in 'Ss':
    n = int(input('Digite um numero: '))
    s += n
    q += 1
    if q == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    r = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
m = s / q
print('Você digitou {} numeros.'.format(q))
print('A soma entre eles é de {}'.format(s))
print('E a média é de {}'.format(m))
print('O maior numero foi {} e o menor foi {}'.format(ma, me))

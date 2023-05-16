maior = 0
menor = 0
for c in range(1, 6):
    a = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        z = maior == a
        z = menor == a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
print('O maior peso lido foi {}'.format(maior))
print('O menor peso lido foi {}'.format(menor))

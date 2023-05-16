a = ('Detergente',1.50,
     'candida',3.00,
     'Desinfetante', 2.50,
     'Lápis', 5.00,
     'Sabão em pó', 4.00)
for pos in range(0, len(a)):
    if pos % 2 == 0:
        print(f'{a[pos]:.<30}', end='')
    else:
        print(f'R$ {a[pos]:>3}')


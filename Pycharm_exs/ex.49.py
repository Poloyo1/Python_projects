n = int(input('Entre com um numero inteiro: '))
print('-='*7)
print(f'Tabuada de {n}')
print('-='*7)
for i in range(1, 11):
    resultado = n * i
    print(f'{n} x {i} = {resultado}')
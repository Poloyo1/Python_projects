a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = 0
while a > b:
    D = b - a
    a = D
    c += 1
print(f'Esses são os valores de {c} e {a}')

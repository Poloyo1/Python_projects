
impar = list()
par = list()
for c in range(0, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
a.append(par[:])
a.append(impar[:])
print('-=' * 50)
print(f'esses foram os numeros pares digitados: {a[0]}')
print(f'Esses foram os numeros impares digitados: {a[1]}')
print('fim')

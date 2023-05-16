a = (int(input('Digite um numero: ')),
     int(input('Digite mais um numero: ')),
     int(input('Digite outro numero: ')),
     int(input('Digite só mais um numero: ')))
num = 0
print(f'Você digitou os valores {a}')
print(f'O valor 9 apareceu {a.count(9)} vezes')
if 3 in a:
     print(f'O numero 3 apareceu na {a.index(3) + 1}° posição')
else:
     print(f'O numero 3 não foi encontrado dentre os numeros que você digitou')
print('Os numeros pares que foram digitados foram: ', end='')
for n in a:
     if n % 2 == 0:
          print(n, end='')


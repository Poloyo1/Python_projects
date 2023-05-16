numerox = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
    'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
res = int(input('Digite um numero, entre 0 e 20: '))
while res not in numeros:
    res = int(input('Desculpe ocorreu um erro, tente novamente: '))
print(f'O numero que você digitou escrito por extenso é {numerox[res]}')

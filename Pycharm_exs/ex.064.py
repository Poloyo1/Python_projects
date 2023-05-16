a = b = soma = 0
print('Esse programa só ira parar quando o numero 999 for digitado')
a = int(input('Digite um numero: '))
while a != 999:
    b += 1
    soma += a
    a = int(input('Digite um numero: '))
print('Fim do programa!')
print('Você digitou {} numeros'.format(b))
print('Essa é a soma dos numeros que vc digitou: {}'.format(soma))


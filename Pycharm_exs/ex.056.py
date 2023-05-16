soma = 0
media = 0
velho = 0
nomev = ' '
mv = 0
print('Analisador de Dados')
for c in range(1, 5):
    a = str(input('Qual é o seu nome? ')).strip()
    b = int(input('Qual é a sua idade? '))
    d = str(input('Qual seu sexo [M/F] ')).strip()
    print('======================================')
    soma += b
    if c == 1 and d in 'Mm':
        velho = b
        nomev = a
    if d in 'Mm' and b > velho:
        velho = b
        nomev = a
    if d in 'Ff' and b < 20:
        mv += 1
media = soma / 4
print('A media de idade do grupo é de {} anos '.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomev))
print('Tem {} mulheres com menos de 20 anos'.format(mv))

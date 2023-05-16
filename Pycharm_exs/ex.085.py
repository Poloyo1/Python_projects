a = list()
b = list()
cont = 0
mai = men = 0
maip = menp = ''
while True:
    b.append(str(input('Digite o seu nome: ')))
    b.append(float(input('Digite o seu peso: ')))
    if len(a) == 0:
        mai = men = b[1]
        maip = menp = b[0]
    else:
        if b[1] > mai:
            mai = b[1]
            maip = b[0]
        if b[1] < men:
            men = b[1]
            menp = b[0]
    a.append(b[:])
    b.clear()
    c = str(input('Gostaria de continuar? [S/N]: ')).upper()
    if c in 'N':
        break
for pe in a:
    cont += 1
print(f'O maior peso foi de {mai}, peso de {maip}')
print(f'O menor peso foi de {men}, peso de {menp}')
print(f'Temos {cont} pessoas cadastradas.')

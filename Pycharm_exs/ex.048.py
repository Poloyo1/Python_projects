soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('Essa é a soma dos  {}, valores solicitados: {}'.format(cont, soma))

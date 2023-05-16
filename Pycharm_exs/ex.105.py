def notas(*num, sit=False):
    cont = 0
    conta = 0
    notinhas = dict()
    for x in num:
        cont += 1
        conta += x
    notinhas['Quantidade de notas'] = cont
    notinhas['Maior'] = max(num)
    notinhas['Menor'] = min(num)
    media = conta / cont
    notinhas['Média'] = media
    if sit:
        if media < 5.0:
            notinhas['Situação'] = 'Ruim'
        if media > 5.0 < 8.0:
            notinhas['Situação'] = 'Razoavel'
        if media > 8.0:
            notinhas['Situação'] = 'Boa'
    return notinhas


print(notas(4, 3, 5, sit=True))

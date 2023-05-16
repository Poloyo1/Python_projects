a = dict()
li = list()
cont = 0
soma = 0
mulheres = list()
while True:
    print('-+' * 40)
    a['Nome'] = str(input('Digite o seu nome: '))
    a['Idade'] = int(input('Digite a sua idade: '))
    a['Sexo'] = str(input('Digite o seu sexo[M/F]: ')).upper()
    if a['Sexo'] in 'F':
        mulheres.append(a['Nome'])
    li.append(a.copy())
    a.clear()
    b = str(input('Quer continuar?[S/N]: ')).upper()
    if b in 'Nn':
        break
print('-+' * 40)
for pe in li:
    cont += 1
    soma += pe['Idade']
media = soma/cont
print(f'Temos {cont} pessoas cadastradas')
print(f'A média de idade do grupo é igual a {media}')
print(f'As mulheres cadastradas foram: {mulheres}')
print('-+' * 40)
print('LISTA DE PESSOAS COM IDADE ACIMA DA MÉDIA')
print('-+' * 40)
for x in li:
    if x['Idade'] > media:
        print(f'Nome = {x["Nome"]}; Idade = {x["Idade"]}; Sexo = {x["Sexo"]}')
        print('')
print('-+' * 40)
print('Fim')
print('-+' * 40)

a = str(input('Digite o nome do aluno: '))
b = float(input(f'Digite a media de {a}: '))
aluno = {'Nome': a, 'Média': b}
if b < 7:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

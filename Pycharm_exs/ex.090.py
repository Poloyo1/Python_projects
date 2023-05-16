a = list()
b = list()
cont = 0
while True:
    b.append(str(input('Digite o nome do aluno: ')))
    b.append(float(input('Digite a nota 1: ')))
    b.append(float(input('Digite a nota 2: ')))
    a.append(b[:])
    b.clear()
    c = str(input('Quer continuar?[S/N]: '))
    if c in 'Nn':
        break
print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":<8}')
print('-' * 30)
for x in a:
    g = x[1] + x[2]
    f = g / 2
    cont += 1
    print(f'{cont} {x[0]:^6} {f:^6}')
while True:
    t = int(input('Mostrar as notas de qual aluno? (999 interrompe):  '))
    if t <= len(a):
        print(f'As notas de {a[t - 1][0]} são {a[t - 1][1]} e {a[t - 1][2]}')
    if t == 999:
        break
print('Fim')
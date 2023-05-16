a = {'Nome': str(input('Nome do jogador: ')), 'Gols': list()}
b = int(input(f'Quantos jogos {a["Nome"]} jogou?:  '))
soma = 0
cont = 0
print('=' * 80)
for c in range(0, b):
    a['Gols'].append(int(input(f'Quantos gols {a["Nome"]} fez na partida {c}: ')))
print('=' * 80)
for x in a['Gols']:
    soma += x
a['Total'] = soma
print(a)
for k, v in a.items():
    print(f'{k} tem o valor de {v}')
print('=' * 80)
print(f'O jogador {a["Nome"]}, jogou {b} partidas')
for d in a['Gols']:
    cont += 1
    print(f'  => Na partida {cont}, fez {d} gols')
print(f'Foi um total de {a["Total"]} gols')
print('=' * 80)

a = dict()
t = list()
cont = 0
soma = 0
while True:
    a['Nome'] = str(input('Digite o nome do jogador: '))
    b = int(input(f'Quantos jogos o jogador {a["Nome"]} jogou? '))
    a['Gols'] = list()
    for c in range(0, b):
        a['Gols'].append(int(input(f'Quantos gols o jogador {a["Nome"]} fez na partida {c + 1}: ')))
    t.append(a.copy())
    a.clear()
    d = str(input('Quer continuar?[S/N]:  ')).upper()
    if d in 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"Gols":<10}{"Total":<6}')
for x in t:
    cont += 1
    for g in x['Gols']:
        soma += g
    print(f'{cont:<4}{x["Nome"]:<10}{x["Gols"]:} {soma:<6}')
while True:
    faria = int(input('Digite o numero do jogador que quer ver os dados(999 interrompe): '))
    if faria - 1 <= len(t):
        print(f'Levantamento de dados do jogador {t[faria-1]["Nome"]}:')
        for c in range(0, b):
            print(f'No jogo {c + 1} fez {t[faria-1]["Gols"][c]} gols')
    elif faria == 999:
        break
    else:
        faria = int(input(f'Erro, não existe nenhum jogador com o codigo {t}, tente novamente: '))
print('Fim')

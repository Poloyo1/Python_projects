def ficha(nome="Desconhecido", gols=0):
    print(f'O jogador {nome}, fez {gols} gol(s) no campeonato')


n = str(input('Digite o nome do jogador: '))
g = str(input('Digite a quantidade de gols que ele fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

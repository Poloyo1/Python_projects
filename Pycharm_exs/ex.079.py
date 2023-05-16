a = []
m = 0
for c in range(0, 4):
    a.append(int(input('Digite um valor: ')))
print(f'O menor numero da lista é {min(a)}')
print(f'o Maior numero da lista é {max(a)}')
print(f'o menor numero da lista está na posição: {a.index(min(a))+1}')
print(f'O maior numero da lista está na posição: {a.index(max(a))+1}')
print(a)

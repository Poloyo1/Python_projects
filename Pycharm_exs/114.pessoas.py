def cadastro(nome, idade):
    pessoas = ['João', 34, 'Luis', 23, 'Marcia', 67]
    pessoas.append(nome)
    pessoas.append(idade)
    for x, i in pessoas:
        print(f'{x}{i:>10}')

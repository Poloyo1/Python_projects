a = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar",
            "trabalhar", "mercado", "programador", "futuro")
b =('a', 'e', 'i', 'o', 'u')
for n in a:
    print(f'{n:<10}', end='')
    for x in b:
        if x in n:
            print(x)
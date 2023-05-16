from EXpack import moeda

p = (float(input('Digite um preço: R$')))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Com um aumento de 10%, fica {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 15%, fica {moeda.diminuir(p, 15, True)}')

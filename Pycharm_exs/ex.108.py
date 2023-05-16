from EXpack import moeda

p = (float(input('Digite um preço: R$')))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Com um aumento de 10%, fica {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 15%, fica {moeda.moeda(moeda.diminuir(p, 15))}')

b = str(input('Digite o seu nome: '))
d = int(input('Digite seu ano de nascimento: '))
f = int(input('Digite sua carteira de trabalho (0 = não tem): '))
a = {'Idade': 2021 - d, 'Nome': b, 'CTPS': f}
if f > 0:
    a['ADC'] = int(input('Digite o ano de contratação: '))
    a['Salario'] = int(input('Digite seu salario R$: '))
    r = (a['Idade'] - (2021 - a['ADC'])) + 35
    a['Aposentadoria'] = r
else:
    a['CTPS'] = 0
print('=' * 80)
for k, v in a.items():
    print(f'  -{k} tem o valor de {v}')
print('=' * 80)

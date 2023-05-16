from datetime import date
atual = date.today().year
meno = 0
maio = 0
for c in range(1, 8):
    a = int(input('Digite o ano de seu nascimento: '))
    b = atual - a
    if b >= 21:
        maio += 1
    else:
        meno += 1
print('Temos {} pessoas Maiores de idade'.format(maio))
print('Temos {} pessoas menores de idade'.format(meno))
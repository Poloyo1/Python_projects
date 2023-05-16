a = []
b = []
c = []
while True:
    d = a.append(int(input('Digite um valor: ')))
    e = str(input('Gostaria de continuar?[S/N] ')).upper()
    if e in 'N':
        break
for x in a:
    if x % 2 == 0:
        b.append(x)
    else:
        c.append(x)
print(a)
print(b)
print(c)

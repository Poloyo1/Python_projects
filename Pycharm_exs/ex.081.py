a = []
for c in range(0, 5):
    b = int(input('Digite um valor: '))
    if c == 0:
        a.append(b)
    elif b > a[len(a)-1]:
        a.append(b)
    else:
        d = 0
        while d < len(a):
            if b <= a[d]:
                a.insert(d, b)
                break
            d += 1
print(a)

def fatorial(a, show=False):
    b = 1
    for c in range(a, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        b *= c
    return b


print(fatorial(5, True))

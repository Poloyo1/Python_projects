a = input('Digite uma expressão: ')
b = []
for c in b:
    if c == '(':
        b.append('(')
    elif c == ')':
        if len(b) > 0:
            b.pop()
        else:
            b.append(')')
            break
if len(b) == 0:
    print('Sua expressão está valida')
else:
    print('Expressão errada')

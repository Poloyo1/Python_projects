b = str(input('Digite seu sexo [F/M]: ')).upper()[0].strip()
while b not in 'MmFf':
    b = str(input('dado invalido digite novamente: [M/F] ')).strip().upper()[0]
print('Fim')

sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MmFm':
    print()
    print('Sexo digitado incorreto!')
    sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
print(sexo)
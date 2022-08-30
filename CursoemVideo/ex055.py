for pessoa in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        menor = peso
        maior = peso
    else:
        if peso>maior:
            maior = peso
        else:
            menor = peso

print('O maior peso lido foi de {} kg'.format(maior))
print('O menor peso lido for de {} kg'.format(menor))


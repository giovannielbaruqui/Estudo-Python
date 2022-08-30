mais_18 = homens = mulheres_20 = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA   ')
    print('-' * 25)
    idade = int(input('Idade: '))

    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]


    print('-' * 25)

    if idade >= 18:
        mais_18 += 1

    if sexo in 'Mm':
        homens += 1

    if sexo in 'Ff':
        if idade < 20:
            mulheres_20 += 1

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break

print('======= FIM DO PROGRAMA =======')
print(f'Total de pessoas com mais de 18 anos: {mais_18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_20} mulheres com menos de 20 anos')






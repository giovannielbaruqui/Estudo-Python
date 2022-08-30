matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior_2linha = soma_3coluna = 0

for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para [{linhas}, {colunas}]: '))

print('-='*30)

for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matriz[linhas][colunas]}]', end='')
        if matriz[linhas][colunas] % 2 == 0:
            soma_pares += matriz[linhas][colunas]
    print()

print('-='*30)

print(f'A soma dos valores pares é de {soma_pares}')

for linhas in range(0, 3):
    soma_3coluna += matriz[linhas][2]

print(f'A soma dos valores da 3ª coluna é de {soma_3coluna}')

for colunas in range(0,3):
    if colunas == 0:
        maior_2linha = matriz[1][colunas]
    elif matriz[1][colunas] > maior_2linha:
        maior_2linha = matriz[1][colunas]

print(f'O maior valor da 2ª linha é {maior_2linha}')

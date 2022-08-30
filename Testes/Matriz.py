matriz = [[0, 0], [0, 0]]

for linhas in range(0, 2):
    for colunas in range(0, 2):
        matriz[linhas][colunas] = int(input(f'Digite o valor para [{linhas}, {colunas}]'))

print('-='*30)

for linhas in range(0, 2):
    for colunas in range(0, 2):
        print(f'[{linhas}, {colunas}]', end='')
    print()
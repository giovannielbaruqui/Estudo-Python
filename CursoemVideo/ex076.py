preços = ('Lápis', 1.75,
          'Borracha', 2,
          'Caderno', 15.90,
          'Estojo', 25,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Canetas', 22.30,
          'Livro', 34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for posição in range(0, len(preços)):
    if posição % 2 == 0: #Nome do produto
        print(f'{preços[posição]:.<30}', end='')
    else:
        print(f'R${preços[posição]:.2f}')
def area(l, c):
    a = l * c
    print(f'A área de um terrono {l} x {c} é de {a}m²')


print(' Controle de Terrenos')
print('-'*20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)

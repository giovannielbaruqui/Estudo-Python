print('-'*30)
print('      LOJA SUPER BARATÃO     ')
print('-'*30)

total = maior_mil = cont = 0
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))

    total += preço

    if preço > 1000:
        maior_mil += 1

    cont += 1
    if cont == 1:
        menor = preço
        nome_menor = produto
    else:
        if preço < menor:
            menor = preço
            nome_menor = produto



    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {maior_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_menor} que custa R${menor:.2f}')
"""
Ler o nome e o peso de várias pessoas
1 - Quantas pessoas foram cadastradas
2 - Lista com as pessoas mais pesadas
3 - Lista com as pessoas mais leves
"""

temp = list()
principal = list()
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    principal.append(temp[:])
    temp.clear()

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}kg. E foi de ', end='')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}', end='')
print()
print(f'O menos peso foi de {menor}kg. E foi de ', end='')
for pessoa in principal:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}', end=' ')
print()
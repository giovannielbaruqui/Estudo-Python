valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    if valores.count(valores[-1]) == 2:
        valores.pop()
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')

    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break

print('-='*15)

valores.sort()
print(f'Você digitou os valores {valores}')

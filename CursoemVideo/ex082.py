"""
Ler vários números e colocar em uma lista
- Imprimir a lista completa
- Imprimir uma lista com os valores Pares
- Imprimir uma lista com os valores Impares
"""

numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um número: ')))

    if numeros[-1] % 2 == 0:
        pares.append(numeros[-1])
    else:
        impares.append(numeros[-1])

    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-='*20)

print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')

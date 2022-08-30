"""
Usuário digitar 7 valores numericos
Manter os valores separados de pares e impares
- Mostrar os valores pares e impares em ordem crescente
"""

numeros = [[], []]
valor = 0

for contador in range(0,7):
    valor = int(input(f'Digite o {contador+1}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-='*30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares foram: {numeros[0]}')
print(f'Os valores impares foram: {numeros[1]}')
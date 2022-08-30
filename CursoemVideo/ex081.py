""" Ler vários números e colocar em uma lista
    1 - Mostrar quantos números foram digitados
    2 - Mostrar a lista ordenada em ordem decrescente
    3 - Se o valor 5 foi digitado e está ou não na lista
"""

numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-='*20)

print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')

if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
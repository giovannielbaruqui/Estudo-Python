"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""


valores = []
for posição in range(0, 5):
    valores.append(float(input(f'Digite um valor para a posição {posição}: ')))

print('=-'*20)

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{indice}...', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == min(valores):
     print(f'{indice}...', end='')

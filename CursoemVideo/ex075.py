números = (int(input('Digite o 1° valor: ')),
           int(input('Digite o 2° valor: ')),
           int(input('Digite o 3° valor: ')),
           int(input('Digite o 4° valor: ')))

print(f'Você digitou os valores {números}')
print(f'O valor nove apareceu {números.count(9)} vezes')
if 3 in números:
    print(f'O valor 3 aparece na {números.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in números:
    if n % 2 == 0:
        print(n, end='')
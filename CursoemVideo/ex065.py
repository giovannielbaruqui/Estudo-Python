soma = cont = 0
resp = 'S'

while resp in 'Ss':
    n = int(input('Digite os números: '))
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = input('Deseja continuar [S/N]? ').upper().strip()[0]
    cont += 1
    soma += n
media = soma/cont
print('A média dos números é igual a {}'.format(media))
print('Maior número digitado: {}'.format(maior))
print('Menor número digitado {}'.format(menor))


n = soma = cont = 0
n = int(input('Digite os números: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite os números: '))

print('Quantidade de números digitados: {}'.format(cont))
print('Soma dos números digitados: {}'.format(soma))


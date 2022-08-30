from random import randint


lista = list()
cont = 0
jogos = list()
quantidade = int(input('Quantas jogos você quer que eu sorteie? '))
total = 0
while total <= quantidade:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        total += 1

for indice, lis in enumerate(jogos):
    print(f'Jogo {indice+1}: {lis}')


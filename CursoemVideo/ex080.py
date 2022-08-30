valores = []
for posição1 in range(0, 5):
    numero = int(input('Digite um valor: '))
    if posição1 == 0 or numero > valores[-1]:
        valores.append(numero)
    else:
        posição2 = 0
        # varrendo a lista
        while posição2 < len(valores):
            if numero <= valores[posição2]:
                valores.insert(posição2, numero)
                break
            posição2 += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')


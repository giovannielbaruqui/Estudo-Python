while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if valor < 0:
        break
    for i in range(1,11,1):
        multiplicação = valor * i
        print(f'{valor} x {i} = {multiplicação}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

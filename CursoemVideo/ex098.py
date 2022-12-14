from time import sleep


def contador(i, f, p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')

    if p < 0:
        p *= -1
    if p == 0:
        p == 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('Fim!')
    print('-=' * 20)


contador(1, 10, 1)
contador(10, 1, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))


opção = 0
while opção != 5:
    print('''
    --------- MENU ---------
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ------------------------''')
    opção = int(input('Opção: '))
    if opção == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1*n2
        print('{} x {} = {}'.format(n1, n2, mult))
    elif opção == 3:
        if n1>n2:
            maior = n1
        elif n2>n1:
            maior = n2
        else:
            maior = n1
        if n1 != n2:
            print('O maior valor é {}'.format(maior))
        else:
            print('Os valores são iguais')
    elif opção == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    else:
        print('Opção Incorreta! Digite novamente!')
    print('=-='*10)
print('Fim do programa!')
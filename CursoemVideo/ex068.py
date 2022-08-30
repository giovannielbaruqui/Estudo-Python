from random import randint

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')

cont = 0
while True:
    print('=-' * 15)
    usuário = int(input('Diga um valor: '))
    par_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 11)
    soma = usuário + computador
    if soma % 2 == 0:
        deu = 'DEU PAR'
    else:
        deu = 'DEU ÍMPAR'
    print('=-' * 15)
    print(f'Você jogou {usuário} e o computador {computador}. Total de {soma} {deu}')
    if par_impar == 'P' and soma % 2 == 0 or par_impar == 'I' and soma % 2 == 1:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        break

print('Você PERDEU!')
print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')
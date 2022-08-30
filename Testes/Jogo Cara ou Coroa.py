from random import randint
pc = randint(0,1)
print('''\033[36m
[ 0 ] Cara
[ 1 ] Coroa\033[m''')
print()
resp = 's'
while resp == 's':
    usu = int(input('Digite qual irá cair: '))
    if pc == usu:
        print('\033[32mParabéns! Você ganhou!\033[m')
    elif pc == 0 and usu == 1:
        print('Você perdeu! Caiu cara!')
    elif pc == 1 and usu == 0:
        print('\033[31mVocê perdeu! Caiu coroa!\033[m')
    print()
    resp = input('Deseja continuar [S/N]: ').lower()
    print()


from random import randint
computador = randint(0,10)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Tente acertar o número (0-10): '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais!')
        elif jogador > computador:
            print('Menos!')
print('Você Acertou! O número correto era {}'.format(computador))
print('Foram necessárias {} tentativas'.format(palpites))
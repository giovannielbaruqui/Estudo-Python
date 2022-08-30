from random import randint
num = randint(0,5)
a = int(input('Tente acertar o número (0-5): '))
if a == num:
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou! O número certo era {}'.format(num))
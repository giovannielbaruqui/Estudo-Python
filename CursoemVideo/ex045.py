from random import randint
pc = randint(1,3)
print('\033[36mPedra, papel e Tesura\033[m')

g = '\033[32mVocê ganhou!\033[m'
p = '\033[31mVocê perdeu!\033[m'
resp='s'
while resp == 's':
    print("""\033[36m
    1: Pedra
    2: Papel
    3: Tesoura
    \033[m""")
    usu = int(input('Digite sua escolha: '))
    if pc == usu:
        print('\033[33mEmpate!!\033[m')
    if pc==1:
        if usu==2:
            print('{} Você: Papel | PC: Pedra'.format(g))
        if usu==3:
            print('{} Você: Tesoura | PC: Pedra'.format(p))
    elif pc==2:
        if usu==1:
            print('{} Você: Pedra | PC: Papel'.format(p))
        if usu==3:
            print('{} Você: Tesoura | PC: Papel'.format(g))
    elif pc==3:
        if usu==1:
            print('{} Você: Pedra | PC: Tesoura'.format(g))
        if usu==2:
            print('{} Você: Papel | PC: Tesoura'.format(p))
    print('')
    resp = input('\033[0;97;46mDeseja continuar [s/n] ?\033[m ').lower()
print('')
print('\033[35mFim de jogo! Obrigado!\033[m')



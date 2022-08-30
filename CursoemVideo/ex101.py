from datetime import date


def voto(ano):
    atual = date.today().year
    idade = atual - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO VOTA')
    elif 18 > idade >= 16 or idade >= 60:
        print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATÓRIO')


ano_nascimento = int(input('Em que ano você nasceu? '))
voto(ano_nascimento)

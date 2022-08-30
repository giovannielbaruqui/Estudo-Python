from datetime import date
ano = int(input('Anos de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade<=9:
    c = 'MIRM'
elif idade<=14:
    c = 'INFANTIL'
elif idade<=19:
    c = 'JUNIOR'
elif idade<=20:
    c = 'SÊNIOR'
else:
    c = 'Master'
print('O atleta tem {} anos.'.format(idade))
print('Classificação:\033[36m {}'.format(c))


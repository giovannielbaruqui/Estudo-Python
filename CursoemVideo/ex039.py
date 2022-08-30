from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade<18:
    print('Não é hora de se alistar!')
    falta = 18 - idade
    print('Faltam {} anos para você se alistar'.format(falta))
elif idade==18:
    print('Hora de se alistar!!')
elif idade>18:
    print('Já passou do tempo de você se alistar!!')
    passou = idade - 18
    print('Já se passaram {} anos do seu alistamento!!'.format(passou))

from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1,8):
    ano_nasc = int(input('Em que ano a {}ª pessoa : '.format(c)))
    idade = atual - ano_nasc
    if idade<18:
        menor = menor + 1
    else:
        maior = maior + 1
print('{} pessoas tem menos que 18 anos.'.format(menor))
print('{} pessoas tem mais que 18 anos.'.format(maior))
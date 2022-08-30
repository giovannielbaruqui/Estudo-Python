# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

somaidade = 0
média_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher20 = 0

for pessoa in range(1,5):
    print('---- {}ª PESSOA ----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade<20:
        total_mulher20 += 1


média_idade = somaidade/4
print('A média de idade do grupo é de {} anos'.format(média_idade))
print('O homem mais velho tem {} anos e se chama {} '.format(maior_idade_homem, nome_velho))
print('Ao todo {} são mulheres e com menos de 20 anos '.format(total_mulher20))




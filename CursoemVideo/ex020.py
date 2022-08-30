from random import shuffle
n1 = input('Digite o nome do 1° aluno: ')
n2 = input('Digite o nome do 2° aluno: ')
n3 = input('Digite o nome do 3° aluno: ')
n4 = input('Digite o nome do 4° aluno: ')
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
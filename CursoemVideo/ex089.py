ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2

    ficha.append([nome, [nota1, nota2], media])

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-='*30)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-'*35)
    opção = int(input('Mostrar notas de qual aluno? (999 interrompe)'))

    if opção == 999:
        print('FINALIZANDO')
        break
    if opção <= len(ficha) - 1:
        print(f'Notas de {ficha[opção][0]} são {ficha[opção][1]}')
salario = float(input('Digite seu salário: '))
if salario > 1250.00:
    aumento = 10/100
    salario_novo = salario + (salario*aumento)
else:
    aumento = 15/100
    salario_novo = salario + (salario*aumento)
print('Seu novo salário é de R${:.2f}'.format(salario_novo))

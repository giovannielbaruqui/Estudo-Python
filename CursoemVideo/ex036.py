casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Quantos anos para pagar? '))
meses = 12*anos
prestacao_mensal = casa/meses
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa,anos,prestacao_mensal))
if (salario*30/100) < prestacao_mensal:
    print('Seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aprovado!')
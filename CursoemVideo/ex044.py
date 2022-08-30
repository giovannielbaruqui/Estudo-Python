preco = float(input('Valor do produto: R$'))
print("""\033[36mOpções:
1: À vista dinheiro/cheque
2: À vista no cartão
3: 2x no cartão
4: 3x no cartão\033[m""")
n = int(input('Digite a opção: '))
if n==1:
    desconto = 10/100
elif n==2:
    desconto = 5/100
elif n==3:
    desconto = 0
elif n==4:
    juros = 20/100
else:
    print('Opção incorreta')
if n<4:
    #com desconto
    final = preco - (preco*desconto)
elif n==4:
    #com juros
    final = preco + (preco*juros)
print('Valor final: R${:.2f}'.format(final))


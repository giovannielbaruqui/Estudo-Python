n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1>n2 and n1>n3:
    maior = n1
elif n2>n3:
    maior = n2
else:
    maior = n3

if n1<n2 and n1<n3:
    menor = n1
elif n2<n3:
    menor = n2
else:
    menor = n3

print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))
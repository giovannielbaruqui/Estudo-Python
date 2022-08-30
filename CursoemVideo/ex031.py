d = float(input('Distância da viagem em km: '))
if d <= 200:
    passagem = d*(0.5)
else:
    passagem = d*(0.45)
print('Preço da passagem: R${:.2f}'.format(passagem))
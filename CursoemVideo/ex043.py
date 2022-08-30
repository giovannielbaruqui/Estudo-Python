peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = peso / (altura**2)
if imc<18.5:
    s = 'Abaixo do peso'
elif imc<25:
    s = 'Peso ideal'
elif imc<=30:
    s = 'Sobrepeso'
elif imc<40:
    s = 'Obesidade'
else:
    s = 'Obesidade mórbida'
print('Situação: {}'.format(s))

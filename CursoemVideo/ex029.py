v = float(input('Velocidade do carro (km/h): '))
if v > 80:
    print('Você foi multado!')
    multa = 7*(v-80)
    print('Valor da multa: R${:.2f}'.format(multa))

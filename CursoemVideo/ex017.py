from math import hypot
ca = float(input('Informe o valor do cateto oposto: '))
co = float(input('Informe o valor do cateto adjacente: '))
hi = hypot(ca,co)
print('A hipotenusa vale {}'.format(hi))

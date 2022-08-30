from math import pi
lado1_retangulo = 5
lado2_retangulo = 7
area_retangulo = lado1_retangulo * lado2_retangulo
raio_circulo = 2
area_circulo = pi*raio_circulo*raio_circulo
area_restante = area_retangulo - area_circulo
print('Área restante = {:.2f}'.format(area_restante))
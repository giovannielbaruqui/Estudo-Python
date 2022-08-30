from math import sqrt
print('ax²+bx+c')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
raiz_delta = sqrt(b*b - 4*a*c)
x1 = (-b + raiz_delta) / (2*a)
x2 = (-b - raiz_delta) / (2*a)
if raiz_delta > 0:
    print('X1 = {}'.format(x1))
    print('X2 = {}'.format(x2))
elif raiz_delta == 0:
    print('Raizes Iguais')
    print('X = {}'.format(x1))
else:
    print('As raízes não são reais!')
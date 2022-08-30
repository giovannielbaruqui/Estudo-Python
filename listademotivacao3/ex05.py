from math import sqrt, pow
x1 = float(input('Digite o x1: '))
y1 = float(input('Digite o y1: '))
x2 = float(input('Digite o x2: '))
y2 = float(input('Digite o y2: '))
d = sqrt(pow(x2-x1,2) + pow(y2-y1,2))
print('A distância entre ({},{}) e ({},{}) é igual a {}'.format(x1,y1,x2,y2,d))

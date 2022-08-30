# Raizes das Funções Polinomiais
# f(x)=2x+1
def poli1(y):
    return (y-1)/2

y = 0
z = poli1(y)

print('f(x)=2x+1')
print(z)

print('-'*30)

#--------------------------------------------

# f(x) = x²-4x+3

import numpy as np

coef = [1,-4,3]

raiz = np.roots(coef)
print('f(x) = x²-4x+3')
print(raiz)

print('-'*30)

#--------------------------------------------

# f(x) = 3x³-11x²+5x+3

import numpy as np

coef = [3,-11,5,3]

raiz = np.roots(coef)
print('f(x) = 3x³-11x²+5x+3')
print(raiz)

print('-'*30)

#--------------------------------------------

# f(x) = 4x³-4x+8

import numpy as np

coef = [3,0,-4,8]

raiz = np.roots(coef)
print('f(x) = 4x³-4x+8')
print(raiz)


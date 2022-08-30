from math import sin, cos, tan, radians
a = float(input('Informe o ângulo que você deseja: '))
print('O seno de {}° é {:.2f} '.format(a, sin(radians(a))))
print('O cosseno de {}° é {:.2f}'.format(a, cos(radians(a))))
print('A tangente de {}° é {:.2f}'.format(a, tan(radians(a))))


#   n = int(input('Digite um número: '))
#   u = n // 1 % 10
#   d = n // 10 % 10
#   c = n // 100 % 10

n = int(input('Digite um número : '))
u1 = n // 1 % 10
d1 = n // 10 % 10
c1 = n // 100 % 10
print('Com %10: {} u, {} d, {} c'.format(u1, d1, c1))

u2 = n // 1
c2 = n // 10
d2 = n // 100

print('Sem %10: {} u, {} d, {} c'.format(u2, c2, d2))




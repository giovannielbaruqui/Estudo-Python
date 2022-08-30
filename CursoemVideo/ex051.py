print('P.A')
n1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
ultimo_termo = n1 + (10-1)*razão
for c in range(n1,ultimo_termo+1,razão):
    print('{}'.format(c), end=" -> ")
print('Acabou!')
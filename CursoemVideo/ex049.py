n = int(input('Digite um valor: '))
print('-'*12)
for c in range(0,11):
    tabuada = c*n
    print('{} x {:2} = {}'.format(n,c,tabuada))
print('-'*12)
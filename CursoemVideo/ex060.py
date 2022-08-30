n = int(input('Digite um número para saber seu fatorial: '))
c = 1
mult = 1
print('{}! = '.format(n), end = '')
while c<n:
    print('{}x'.format(c), end = '')
    mult = mult * c
    c += 1
mult *= n
print('{} = {}'.format(n, mult))
a1 = int(input('1° termo: '))
razão = int(input('Razão da P.A: '))

n = 1
while n<=10:
    an = a1 + (n-1)*razão
    print(an, end=' ')
    n += 1

números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0-20: '))
    if 0<=n<=20:
        break
    print('Você digitou o número errado!', end = ' ')
print(f'Você digitou o número {números[n]}')
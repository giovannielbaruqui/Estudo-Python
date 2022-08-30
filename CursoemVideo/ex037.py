n = int(input('Digite um número para conversão: '))
print("""\033[36m
1: Binário
2: Octal
3: Hexadecial\033[m""")
opção = int(input('Tipo de conversão: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n,bin(n)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n,oct(n)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))
else:
    print('Opção inválida! Tente novamente!')

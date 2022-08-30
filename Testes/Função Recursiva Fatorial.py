#def nome(parâmetros):
#    sequência de comandos
#    return nome(própria função)

def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1)

num = int(input('Número: '))
resultado = fat(num)
print(resultado)
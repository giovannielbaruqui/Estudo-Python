nome = input('Digite seu nome completo: ').strip()
print('Nome todo em maíusculo: {}'.format(nome.upper()))
print('Nome todo em minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome.replace(' ', ''))))
nome1 = nome.split()
print('Quantidade de letras do 1° nome: {}'.format(len(nome1[0])))

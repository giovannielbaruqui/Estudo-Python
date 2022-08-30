n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('Sua média foi \033[4m{:.1f}\033[m'.format(media))
if media<5:
    situacao = '\033[31mREPROVADO\033[m'
elif media<7:
    situacao = '\033[33mRECUPERAÇÃO\033[m'
else:
    situacao = '\033[32mAPROVADO\033[m'
print(situacao)

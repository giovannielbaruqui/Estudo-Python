frase = input('Digite uma frase: ').strip().lower()
print('Quantidade de vezes que aparece a letra a: {}'.format(frase.count('a')))
print('Posição que aparece o primeiro a: {}'.format(frase.find('a')+1))
print('Posição que aparece o último a: {}'.format(frase.rfind('a')+1))

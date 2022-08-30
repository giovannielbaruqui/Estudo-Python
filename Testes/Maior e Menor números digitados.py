for vezes in range(1,5):
    número = int(input('Digite o {}° número: '.format(vezes)))
    #Define o maior e o menor número primeiro pelo primeiro número digitado
    # para usar como base de comparação
    if vezes == 1: #Define a 1ª vez
        menor = número
        maior = número
    else: #Para as vezes seguintes
        if número>maior: #Confere o 2°, 3°, ... digitado e verifica se é mair que digitado antes
            maior = número
        else:
            menor = número
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))
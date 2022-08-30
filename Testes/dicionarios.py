estado = dict()
brasil = list()
for contador in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for estados in brasil:
    for values in estados.items():
        print(values)
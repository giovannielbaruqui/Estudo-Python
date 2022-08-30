"""
Ler o [nome], [ano de nascimento] (cadastrar como [idade]) e [carteira de trabalho]
Se a [carteira de trabalho] for diferente de 0:
    O dicionário receberá também o [ano de contratação] e o [salário]
Calcular e acrescentar com quantos anos a pessoa irá se aposentar
"""
from datetime import datetime
dados = dict()

dados['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano_nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = (dados['contratação'] + 35) - ano_nasc

print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem valor {v}')
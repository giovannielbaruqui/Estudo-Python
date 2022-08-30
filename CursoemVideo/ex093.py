"""
Ler o [nome] do jogador e quantas [partidas] ele jogou
Ler a quantidade de [gols em cada partida]
Adicionar tudo isso a um dicionário, incluindo o [total de gols] feitos durante o campeonato
"""

jogador = dict()
gol = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gol.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for c in range(0, partidas):
    print(f'     => Na partida {c}, fez {gol[c]} gols. ')
print(f'Foi um total de {jogador["total"]} gols.')
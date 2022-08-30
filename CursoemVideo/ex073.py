times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR',  'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

a =('-='*45)

# Cinco primeiros times
print(a)
print(f'Os cinco primeiros times são: {times[:5]}')

# Últimos 4 colocados
print(a)
print(f'Os quatro últimos colocados são: {times[-4:]}')

# Times em ordem alfabética
print(a)
print(f'Ordem alfabética dos times: {sorted(times)}')

# Posição em que Chapecoense está:
print(a)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
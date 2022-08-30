# Tuplas podem determinadas por '()', porém não precisam colocar nada, mas é recomendável
# Tuplas são imutáveis
# Listas são determinadas por '[]'
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#              0          1        2        3
#             -4         -3       -        -1

# 1

print('-=1=-')
print()
print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])
print(lanche[-3:])
print(lanche)
print(len(lanche))

print('-'*50)

# 2
# Imprime a tupla sem '[]'

print('-=2=-')
print()

for comida in lanche:
    print(comida, end=' ')
print()

print('-'*50)

# 3
#

print('-=3=-')
print()

for cont in range(0, len(lanche)):
    print(lanche[cont], end =' ')
print()

print('-'*50)

# 4
#

print('-=4=-')
print()

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} posição {cont}')

print('-'*50)

#5
#
print('-=5=-')
print()

for posição, comida in enumerate(lanche):
    print(f'{comida} posição {posição}')

print('-'*50)

# 6
# Coloca na ordem

print('-=6=-')
print()

print(sorted(lanche))

#
print()


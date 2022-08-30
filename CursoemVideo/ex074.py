from random import randint

números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os números digitados foram: ', end='')
for n in números:
    print(n, end=' ')
print(f'\nO maior valor foi {max(números)}')
print(f'O menor valor foi {min(números)}')
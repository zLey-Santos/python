from random import randint

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os Valores Sorteados Foram: ', end=' ')

for n in num:
  print(f'{n}', end=' ')

print()
print(f'O maior número sorteado foi {max(num)}')
print(f'O menor número sorteado foi {min(num)}')

num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
  if num % c == 0:
    print(f'\033[33m', end=' ')
    tot += 1
  else:
    print(f'\033[31m', end=' ')
  print(f'{c}\033[m', end = ' ')
print(f'\n(O número \033[32m{num}\033[m foi divisível por \033[36m{tot}\033[m vezes)')
if tot == 2:
  print(f'\033[1;32m O número \033[33m{num}\033[m \033[32m É primo\033[m')
else:
  print(f'\033[1;31m O Número \033[36m{num}\033[36m \033[1;31m Não é primo\033[m')
  
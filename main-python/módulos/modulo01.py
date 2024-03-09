from math import sqrt, floor, ceil

num = float(input('Digite um número: '))
up = sqrt(num)
print(f'O valor de {num:.0f} aredondado para cima é {ceil(up)}')
print(f'O valor de {num:.0f} aredondado para baixo é {floor(up)}')

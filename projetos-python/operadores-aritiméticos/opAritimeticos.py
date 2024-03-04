# Ordem de precedência dos Operadores Aritméticos:
# 1- () Primeiro, tudo que está entre parênteses ().
# 2- ** Segundo, tudo que for elevado à potência.
# 3- *, /, //, % Conjunto de operadores: * Multiplicação, / Divisão, // Divisão inteira, % Módulo, Resto da divisão.
# 4- +, - Por último, ficam os operadores de + Adição e - Subtração.

oA1 = 5 + 3 * 2
print(f'Resultado {oA1}')

oA2 = 3 * 5 + 4 ** 2
print(f'Resultado {oA2}')

oA3 = 3 * (5 + 4) ** 2
print(f'Resultado {oA3}')

# Para encontrar raízes quadradas, basta elevar o número desejado à metade: 81 ** (1/2) == 9.
# O mesmo para raízes cúbicas: basta elevar a 81 ** (1/3) == 4.3267487109222245.

rz1 = 81 ** (1 / 2)
print(f'A raiz quadrada é {rz1}')

rz2 = 81 ** (1 / 3)
print(f'A raiz cúbica é {rz2}')

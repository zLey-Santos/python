# math.ceil(x): Retorna o menor número inteiro maior ou igual a x. Ou seja, faz o arredondamento para cima.
# math.floor(x): Retorna o maior número inteiro menor ou igual a x. Ou seja, faz o arredondamento para baixo.
# math.trunc(x): Elimina a parte fracionária de x e retorna o inteiro resultante.
# math.pow(x, y): Retorna x elevado à potência y.
# math.sqrt(x): Retorna a raiz quadrada de x.
# math.factorial(x): Retorna o fatorial de x.
import math

# Arredondamento para cima (Ceil)
valor = 2.145
arredondamento_cima = math.ceil(valor)
print(f'Arredondamento para cima de {valor}: {arredondamento_cima}')

# Arredondamento para baixo (Floor)
valor = 2.145
arredondamento_baixo = math.floor(valor)
print(f'Arredondamento para baixo de {valor}: {arredondamento_baixo}')

# Eliminar os números após a vírgula (Trunc)
valor = 2.1
sem_decimal = math.trunc(valor)
print(f'Sem números após a vírgula de {valor}: {sem_decimal}')

# Potência (Pow)
base = 2
expoente = 3
potencia = math.pow(base, expoente)
print(f'{base} elevado a {expoente}: {potencia}')

# Raiz quadrada (Sqrt)
numero = 9
raiz_quadrada = math.sqrt(numero)
print(f'Raiz quadrada de {numero}: {raiz_quadrada}')

# Fatorial (Factorial)
numero = 5
fatorial = math.factorial(numero)
print(f'Fatorial de {numero}: {fatorial}')

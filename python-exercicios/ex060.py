# Solicita a entrada de um número inteiro para calcular o fatorial
num = int(input('Digite um número para calcular o fatorial: '))

# Inicializa as variáveis para o cálculo do fatorial
cont = num
fatorial = 1

# Exibe a expressão do fatorial sendo calculado
print(f'Calculando {num}! =', end=' ')

# Loop while para calcular o fatorial
while cont > 0:
    # Exibe o número atual do fatorial
    print(f'{cont}', end=' ')
    # Exibe o operador multiplicativo se houver mais números a serem multiplicados
    print(f'*' if cont > 1 else '=', end=' ')
    # Calcula o fatorial multiplicando os números de forma decremental
    fatorial *= cont
    # Decrementa o contador
    cont -= 1
# Exibe o resultado final do fatorial
print(f'{fatorial}')


'''
from math import factorial
n = int(input('Digite um número para \ncalcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')
'''


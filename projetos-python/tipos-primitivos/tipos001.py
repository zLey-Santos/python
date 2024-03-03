# Os quatro tipos primitivos básicos em Python são:
# 1. int: é um tipo primitivo para números inteiros.
# 2. float: é um tipo primitivo para números reais ou de ponto flutuante, por exemplo, 1.2.
# 3. bool: é um tipo primitivo para boolean/lógicos True ou False. Sempre inicie com letra maiúscula ao usar um valor lógico.
# 4. str: é um tipo primitivo para strings/caracteres.

# Temos vários métodos .isalnum() verificar se é alfanumérico... etc

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2

# Ambas as formas de imprimir o resultado são válidas, mas a primeira opção usando
# f-string (print(f'A soma entre {n1} e {n2} é igual a {s}.'))
# é geralmente preferida por ser mais legível e mais fácil de escrever.
print(f'A soma entre {n1} e {n2} é igual a {s}.')
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

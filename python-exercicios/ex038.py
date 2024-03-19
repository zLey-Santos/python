print(f'{'==' * 10} Comparando números v.2 {'==' * 10} ')

# Solicita ao usuário que insira dois números inteiros e os converte para inteiros.
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

# Verifica se o primeiro número é maior que o segundo número.
if n1 > n2:
   # Se o primeiro número for maior, imprime que o primeiro valor é maior.
   print(f'O PRIMEIRO valor é maior.')
# Verifica se o segundo número é maior que o primeiro número.
elif n2 > n1:
   # Se o segundo número for maior, imprime que o segundo valor é maior.
   print(f'O SEGUNDO valor é maior.')
else:
   # Se ambos os números forem iguais, imprime que os valores são iguais.
   print('Os valores são IGUAIS.')

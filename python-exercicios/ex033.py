# Solicitar ao usuário três valores inteiros e atribuí-los às variáveis n1, n2 e n3.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

# Encontrar o maior e o menor valor entre n1, n2 e n3 usando as funções max() e min().
maior_valor = max(n1, n2, n3)
menor_valor = min(n1, n2, n3)

# Exibir os resultados.
print(f"O maior valor digitado foi {maior_valor} \n"
      f"O menor valor digitado foi {menor_valor}")

print('--'*16)

# Solicitar ao usuário novamente três valores inteiros e atribuí-los às variáveis a, b e c.
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Inicializar as variáveis 'menor' e 'maior' com o primeiro valor digitado (a).
menor = a
maior = a

# Verificar qual valor é o menor entre a, b e c.
if b < menor:
    menor = b
if c < menor:
    menor = c

# Verificar qual valor é o maior entre a, b e c.
if b > maior:
    maior = b
if c > maior:
    maior = c

# Exibir os resultados.
print(f'O valor maior digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')

# Recebe quatro números inteiros do usuário e armazena em uma tupla
num = (int(input('Digite primeiro número: ')), 
       int(input('Digite segundo número: ')), 
       int(input('Digite terceiro número: ')), 
       int(input('Digite quarto número: ')))

# Exibe os números digitados pelo usuário
print(f'Você digitou os valores {num}')

# Conta quantas vezes o número 9 aparece na tupla e exibe o resultado
print(f'O valor 9 apareceu {num.count(9)} vezes')

# Encontra e exibe o maior número digitado pelo usuário
print(f'O maior número digitado foi {max(num)}')

# Verifica se o número 3 está presente na tupla
if 3 in num: 
    # Exibe a posição da primeira ocorrência do número 3 (adicionando 1 para mostrar a posição correta)
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    # Informa que o número 3 não foi digitado
    print('O valor 3 não foi digitado')

# Cria uma lista contendo apenas os números pares da tupla
pares = ([n for n in num if n % 2 == 0])

# Verifica se existem números pares na lista
if pares:
    # Exibe os números pares encontrados, separados por vírgulas
    print(f'Os valores pares digitados foram: {", ".join(map(str, pares))}')
else:
    # Informa que não foram encontrados números pares
    print('Sem valores pares encontrados')

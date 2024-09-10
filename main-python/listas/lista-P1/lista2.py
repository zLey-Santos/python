# Cria uma lista vazia para armazenar os valores inseridos pelo usuário
valores = list()

# Laço que se repete 5 vezes, pedindo ao usuário para inserir valores
for cont in range(0, 5):
    # Adiciona o valor digitado pelo usuário à lista 'valores'
    valores.append(int(input('Digite um valor: ')))

# Exibe o cabeçalho para as colunas de posição (CH) e valor (VL) com formatação
print(f'{" "*11}CH {" "*13}VL')

# Itera sobre a lista 'valores', obtendo o índice (c) e o valor (v) de cada elemento
for c, v in enumerate(valores):
    # Exibe a posição (c) e o valor correspondente (v) de cada elemento da lista
    print(f'Na posição {c} temos o valor {v}! ')

# Indica que chegou ao final da lista
print('Cheguei no final da lista.')

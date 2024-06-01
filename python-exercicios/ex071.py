# Solicita ao usuário que digite o valor a ser sacado
valor = int(input('Qual valor você quer sacar? R$'))

# Inicializa as variáveis para contagem das notas
total = valor
notas = [50, 20, 10, 1]  # Lista de tipos de notas disponíveis
contagem_notas = {}  # Dicionário para armazenar a quantidade de cada nota

# Loop para calcular a quantidade de cada nota
for nota in notas:
    if total >= nota:
        contagem_notas[nota] = total // nota
        total %= nota

# Imprime a quantidade de cada nota
print('Você receberá:')
for nota, quantidade in contagem_notas.items():
    print(f'{quantidade} nota(s) de R${nota}')


# Usando while:

# Solicita ao usuário que digite o valor a ser sacado
valor = int(input('Qual valor você quer sacar? R$'))

# Inicializa as variáveis para contagem das notas
total = valor
nota = 50  # Começa com a maior nota disponível
contagem_notas = {}  # Dicionário para armazenar a quantidade de cada nota

# Loop para calcular a quantidade de cada nota
while total > 0:
    if total >= nota:
        # Calcula quantas notas são necessárias e armazena no dicionário
        qtd_notas = total // nota
        contagem_notas[nota] = qtd_notas
        total -= qtd_notas * nota  # Atualiza o total restante
    # Atualiza para a próxima nota menor
    if nota == 50:
        nota = 20
    elif nota == 20:
        nota = 10
    elif nota == 10:
        nota = 1

# Imprime a quantidade de cada nota
print('Você receberá:')
for nota, quantidade in contagem_notas.items():
    print(f'{quantidade} nota(s) de R${nota}')

# Inicializa a lista que armazenará os números inseridos pelo usuário
listnum = []

# Variáveis para armazenar o maior e o menor valor encontrados
big = 0
small = 0

# Listas para armazenar os índices das posições dos maiores e menores valores
big_indices = [0]
small_indices = [0]

# Loop para solicitar ao usuário a entrada de 5 valores
for c in range(0, 5):
    # Adiciona o valor digitado pelo usuário na lista 'listnum'
    listnum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    
    # Caso seja a primeira iteração, define o primeiro valor como o maior e o menor
    if c == 0:
        big = small = listnum[c]
    else:
        # Verifica se o valor atual é maior que o maior valor encontrado até agora
        if listnum[c] > big:
            big = listnum[c]  # Atualiza o maior valor
            big_indices = [c]  # Atualiza a lista de índices com a nova posição do maior valor
        # Caso o valor seja igual ao maior, adiciona o índice à lista de índices do maior valor
        elif listnum[c] == big:
            big_indices.append(c)  

        # Verifica se o valor atual é menor que o menor valor encontrado até agora
        if listnum[c] < small:
            small = listnum[c]  # Atualiza o menor valor
            small_indices = [c]  # Atualiza a lista de índices com a nova posição do menor valor
        # Caso o valor seja igual ao menor, adiciona o índice à lista de índices do menor valor
        elif listnum[c] == small:
            small_indices.append(c)  

# Exibe uma linha de separação para a saída dos resultados
print('=-'*30)  

# Exibe os valores digitados pelo usuário
print(f'Os valores digitados são: {listnum}')

# Exibe o maior valor encontrado e suas respectivas posições na lista
print(f'O MAIOR valor digitado foi: {big} na(s) posição(ões) do índice {", ".join(map(str, big_indices))}')
# Exibe o menor valor encontrado e suas respectivas posições na lista
print(f'O MENOR valor digitado foi: {small} na(s) posição(ões) do índice {", ".join(map(str, small_indices))}')

# Exibe uma linha de separação final
print('=-'*30)  

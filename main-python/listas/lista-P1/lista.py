# Cria uma lista com quatro elementos: 2, 5, 9 e 1
num = [2, 5, 9, 1]

# Altera o valor do terceiro elemento (índice 2) da lista de 9 para 3
num[2] = 3

# Adiciona o número 7 ao final da lista
num.append(7)

# Ordena a lista em ordem decrescente
num.sort(reverse=True)

# Insere o valor 0 na posição de índice 2 (terceira posição)
num.insert(2, 0)

# Remove o elemento na posição de índice 2 (o valor que foi inserido anteriormente)
num.pop(2)

# Exibe a lista atualizada
print(num)

# Exibe o tamanho da lista, ou seja, o número de elementos que ela contém
print(f'Essa lista tem {len(num)} elementos.')

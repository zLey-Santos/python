# Divisão de Strings em Python

frase = 'Curso em Vídeo Python'

# frase.split(): Divide a string em substrings usando os espaços em branco como delimitadores.
# Retorna uma lista contendo as substrings.
# Saída: ['Curso', 'em', 'Vídeo', 'Python']
print(frase.split())

# Atribuímos a lista de palavras resultante da divisão à variável lista_palavras
lista_palavras = frase.split()

# Junção de Strings em Python

# '-'.join(lista_palavras): Junta os elementos da lista usando '-' como separador entre cada elemento.
# Retorna uma nova string contendo os elementos unidos.
# Saída: Curso-em-Vídeo-Python
print('-'.join(lista_palavras))

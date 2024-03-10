# Fatiamento em Python

# Suponha a frase 'Curso em Video Python'
frase = 'Curso em Video Python'

# Exemplo 1: [9:13]
# Aqui, vamos pegar a parte da frase começando do índice 9 até o índice 13 (o 14 é exclusivo)
# Resultado: 'Vide'

print(frase[9:13])

# Exemplo 2: [9:21:2]
# Começamos no índice 9 e terminamos no índice 20 (21 é exclusivo), pulando de 2 em 2
# Resultado: 'VdoPto'

print(frase[9:21:2])

# Exemplo 3: [:5]
# Aqui, começamos do início e vamos até o índice 4 (5 é exclusivo)
# Resultado: 'Curso'

print(frase[:5])

# Exemplo 4: [15:]
# Começamos no índice 15 e vamos até o final da frase
# Resultado: 'Python'

print(frase[15:])

# Exemplo 5: [9::3]
# Começamos no índice 9, vamos até o final, pulando de 3 em 3
# Resultado: 'ViePh'

print(frase[9::3])

# Transformação de Strings em Python

frase = 'Curso em Vídeo Python'

# frase.replace('Python', 'Android'): Substitui todas as ocorrências da substring 'Python' por 'Android'.
# Retorna uma nova string com a substituição.
print(frase.replace('Python', 'Android'))

# frase.upper(): Converte todos os caracteres da string para maiúsculas.
print(frase.upper())

# frase.lower(): Converte todos os caracteres da string para minúsculas.
print(frase.lower())

# frase.capitalize(): Converte o primeiro caractere da string para maiúscula e os demais para minúsculas.
print(frase.capitalize())

# frase.title(): Converte o início de cada palavra na string para maiúscula.
print(frase.title())

# Removendo espaços em branco extras

frase1 = '   Aprendendo Python  '
print(frase1)

# frase1.strip(): Remove espaços em branco extras do início e do final da string.
print(frase1.strip())

# len(frase1) retorna 22, incluindo espaços em branco no início e no final.
print(f'Tamanho da frase {len(frase1)}')

# len(frase1.rstrip()): Retorna 20, removendo os dois espaços em branco do final da string.
print(f'Remove os espaços da direita {len(frase1.rstrip())}')

# len(frase1.lstrip()): Retorna 20, removendo os espaços em branco do início da string.
print(f'Remove os espaços da esquerda {len(frase1.lstrip())}')

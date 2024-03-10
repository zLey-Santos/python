# Análise de Strings em Python

frase = 'Curso em Vídeo Python'

# len(frase): Retorna o comprimento da string, ou seja, o número de caracteres.
# Neste caso, a frase tem 21 caracteres.
print(len(frase))

# frase.count('o', 0, 13): Conta quantas vezes o caractere 'o' aparece na frase entre os índices 0 e 12 (13 é exclusivo).
# Neste caso, há apenas 1 'o' nesse intervalo.
print(frase.count('o', 0, 13))

# frase.find('deo'): Retorna o índice onde a substring 'deo' começa pela primeira vez na frase.
# Neste caso, 'deo' começa no índice 11.
print(frase.find('deo'))

# frase.find('Android'): Retorna -1 se a substring não for encontrada na frase.
# Neste caso, 'Android' não está na frase, então retorna -1.
print(frase.find('Android'))

# 'Curso' in frase: verifica se a substring 'Curso' está presente na frase.
# Retorna True se estiver presente, caso contrário, retorna False.
# Neste caso, 'Curso' está na frase, então retorna True.
print('Curso' in frase)

import random
nomes = ['Ana', 'Pepe', 'Bruna', 'zLey']
input('Pressione ENTER para ver a ordem de apresentação dos trabalhos: ')
random.shuffle(nomes)
print(f'A ordem de apresentação dos trabalhos são: {nomes}')

# O método shuffle() pertence ao módulo random em Python é usado para embaralhar os elementos de uma sequência de forma aleatória.

from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
nomes = [n1, n2, n3, n4]
input('Pressione ENTER para ver a ordem de apresentação dos trabalhos: ')
shuffle(nomes)
print(f'A ordem de apresentação dos trabalhos são: {nomes}')

# O método shuffle() pertence ao módulo random em Python é usado para embaralhar os elementos de uma sequência de forma aleatória.

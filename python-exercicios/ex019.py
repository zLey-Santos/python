from random import choice
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Primeiro Aluno: '))
n3 = str(input('Primeiro Aluno: '))
n4 = str(input('Primeiro Aluno: '))
lista = [n1, n2, n3, n4]
nome_aluno = choice(lista)
print(f'O aluno escolhido é: {nome_aluno}')

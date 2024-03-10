import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Primeiro Aluno: '))
n3 = str(input('Primeiro Aluno: '))
n4 = str(input('Primeiro Aluno: '))
lista = [n1, n2, n3, n4]
escolha = input('Pressione ENTER para escolher um nome aleatorio):')
nome_aluno = random.choice(lista)
print(f'O aluno escolhido é: {nome_aluno}')

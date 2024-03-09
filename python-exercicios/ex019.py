import random

nomes = ['Ana', 'Miguel', 'Lucia', 'Adam']
escolha = input('Pressione ENTER para escolher um nome aleatorio):')
nome_aluno = random.choice(nomes)
print(f'O aluno escolhido é: {nome_aluno}')

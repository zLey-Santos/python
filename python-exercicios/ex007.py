nome = input('Digite o nome do aluno: ')
n1 = float(input(f'Digite a primeira nota do aluno {nome}: '))
n2 = float(input(f'Digite a segunda nota do aluno {nome}: '))
m = (n1 + n2) / 2
print(f'A média entre as {n1} e {n2} do aluno {nome} é igual a {m:.1f}')

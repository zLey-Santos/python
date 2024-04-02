# Inicializa as variáveis de controle
soma_idade = 0
media_idade = 0
maior_idade_h = 0
nome_velho = ''
tot_mulher20 = 0

# Loop for para iterar sobre as 4 pessoas
for p in range(1, 4 + 1):
    print(f'----- {p}ª -----')
    # Solicita os dados da pessoa atual
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    # Soma as idades para calcular a média posteriormente
    soma_idade += idade
    
    # Verifica se é a primeira pessoa e se é um homem para inicializar o maior_idade_h e nome_velho
    if p == 1 and sexo in 'Mm':
        maior_idade_h = idade
        nome_velho = nome
    # Verifica se a pessoa atual é um homem e se sua idade é maior que a maior idade registrada
    if sexo in 'Mm' and idade > maior_idade_h:
        maior_idade_h = idade
        nome_velho = nome
    # Verifica se a pessoa atual é uma mulher com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1

# Exibe a quantidade de mulheres com menos de 20 anos
if tot_mulher20 == 0:
    print()
elif tot_mulher20 > 1:
    print(f'Temos {tot_mulher20} mulheres com menos de 20 anos.')
else:
    print(f'Temos {tot_mulher20} mulher com menos de 20 anos.')
# Calcula a média de idade
media_idade = soma_idade / 4
print(f'A média de idade é de {media_idade} anos.')
# Exibe a idade e o nome do homem mais velho
print(f'O homem mais velho tem {maior_idade_h} anos e se chama {nome_velho}.')

# Solicita ao usuário que digite o salário atual do funcionário e converte para float.
salario = float(input('Digite o salário atual do funcionário: '))

# Dicionário contendo códigos ANSI para cores usadas na formatação de saída.
# 'Limpa' é usado para limpar a formatação de cores, 'sal' e 'R$' são usados para colorir o texto.
cores = {
    'limpa': '\033[m',
    'salario': '\033[1:31m',  # Vermelho brilhante para destacar o valor do salário
    'R$': '\033[1:32m'  # Verde brilhante para destacar a moeda R$
}

# Verifica se o salário é maior que 5000.
if salario > 5000:
    # Calcula o reajuste de 10% no salário.
    reajuste_10 = (salario * 10 / 100) + salario
    # Exibe o novo salário com reajuste de 10% destacando a moeda e o valor em vermelho.
    print(f'O seu salário passa a ser de '
          f'{cores["R$"]}R${cores["salario"]}{reajuste_10:.2f}{cores["limpa"]},'
          f' 10% de reajuste!')
else:
    # Calcula o reajuste de 15% no salário.
    reajuste_15 = (salario * 15 / 100) + salario
    # Exibe o novo salário com reajuste de 15% destacando a moeda e o valor em vermelho.
    print(f'O seu salário passa a ser de '
          f'{cores["R$"]}R${cores["salario"]}{reajuste_15:.2f}{cores["limpa"]},'
          f' 15% de reajuste')

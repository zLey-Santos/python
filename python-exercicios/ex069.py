# Inicializa os contadores para:
# tot18 - número de pessoas com 18 anos ou mais
# totH - número de homens cadastrados
# totM - número de mulheres com menos de 20 anos
tot18 = totH = totM = 0

# Loop infinito para coletar dados até que o usuário decida parar
while True:
    # Solicita a idade do usuário e converte a entrada para um inteiro
    idade = int(input('Idade: '))

    # Inicializa a variável 'sexo' com um espaço em branco
    sexo = ' '
    # Loop para garantir que o usuário escolha 'M' para masculino ou 'F' para feminino
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()

    # Verifica se a idade é maior ou igual a 18 anos
    if idade >= 18:
        tot18 += 1  # Incrementa o contador de pessoas com 18 anos ou mais

    # Verifica se o sexo é masculino
    if sexo == 'M':
        totH += 1  # Incrementa o contador de homens cadastrados

    # Verifica se o sexo é feminino e a idade é menor que 20 anos
    if sexo == 'F' and idade < 20:
        totM += 1  # Incrementa o contador de mulheres com menos de 20 anos

    # Inicializa a variável 'resp' com um espaço em branco
    resp = ' '
    # Loop para garantir que o usuário escolha 'S' para sim ou 'N' para não
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip().upper()
    # Verifica se o usuário escolheu parar
    if resp == 'N':
        break  # Interrompe o loop se o usuário escolher parar

# Imprime o total de pessoas com 18 anos ou mais
print(f'Total de pessoas com mais de 18 anos: {tot18}')
# Imprime o total de homens cadastrados
print(f'Ao todo temos {totH} homens cadastrados')
# Imprime o total de mulheres com menos de 20 anos
print(f'Temos {totM} mulheres com menos de 20 anos')

# Inicializa as variáveis maior e menor com 0
maior = 0
menor = 0

# Loop for para iterar sobre as 5 pessoas
for p in range(1, 5 + 1):
    # Solicita o peso da pessoa atual
    peso = float(input(f'Peso da {p}ª pessoa: '))

    # Verifica se é a primeira pessoa
    if p == 1:
        # Se for a primeira pessoa, define o peso como maior e menor
        maior = peso
        menor = peso
    else:
        # Se não for a primeira pessoa, compara o peso com o maior e o menor até o momento
        # Atualiza o valor de maior, se necessário
        if peso > maior:
            maior = peso
        # Atualiza o valor de menor, se necessário
        if peso < menor:
            menor = peso

# Após iterar sobre todas as pessoas, exibe o maior e o menor peso
print(f'O maior peso foi de {maior}Kg\nO menor peso foi de {menor}Kg.')

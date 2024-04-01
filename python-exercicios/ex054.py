from datetime import date
print(f'{"==" * 5}MAIORIDADE{"==" * 5}')

# Obtém o ano atual
ano_atual = date.today().year
# Inicializa contadores
maior = 0
menor = 0
# Loop para iterar sobre as 7 pessoas
for pessoas in range(1, 8):
    # Solicita o ano de nascimento da pessoa
    ano_nasc = int(input(f'Em que ano a {pessoas}ª pessoa nasceu? '))
    # Calcula a idade da pessoa
    idade = ano_atual - ano_nasc
    # Verifica se a pessoa é maior de idade
    if idade >= 21:
        maior += 1  # Incrementa o contador de maiores de idade
    else:
        menor += 1  # Incrementa o contador de menores de idade
# Exibe o total de pessoas maiores de idade
print(f'Total de pessoas com mais de 21 anos: \033[34m{maior} São maiores de idade\033[m')
# Exibe o total de pessoas menores de idade
print(f'Total de pessoas com menos de 21 anos: \033[32m{menor} São menores de idade\033[m')

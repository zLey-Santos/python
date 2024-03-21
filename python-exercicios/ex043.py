# Imprime um cabeçalho com o título do programa
print(f'{"==" * 10}\033[33m[ÍNDICE DE MASSA CORPORAL]\033[m{"==" * 10}')

# Solicita ao usuário que insira o peso em Kg e a altura em metros
peso = float(input('Indique o seu peso em (Kg): '))
altura = float(input('Indique a sua altura em (m): '))

# Define um dicionário com códigos ANSI para cores usadas na formatação de saída
cor = {
    'L': '\033[m',      # Cor padrão
    'I': '\033[31m',    # Cor vermelha
    'PA': '\033[34m',   # Cor azul
    'IA': '\033[35m'    # Cor roxa
}

# Imprime uma mensagem indicando o início do cálculo do IMC
print(f'{"__" * 10}[IMC]{"__" * 10}')

# Calcula o IMC
imc = peso / (altura ** 2)

# Imprime o peso e a altura fornecidos pelo usuário
print(f'O seu peso é de {cor["PA"]}{peso:.2f}{cor["L"]} Kg\n'
      f'A sua altura é de {cor["PA"]}{altura}{cor["L"]} m')

# Verifica o intervalo de IMC e imprime a classificação correspondente
if imc < 18.5:
    print(f'O seu IMC é de {cor["IA"]}{imc:.2f}{cor["L"]} {cor["I"]}[Abaixo do peso].')
elif 18.5 <= imc < 25:
    print(f'O seu IMC é de {cor["IA"]}{imc:.2f}{cor["L"]} {cor["I"]}[Peso ideal].')
elif 25 <= imc < 30:
    print(f'O seu IMC é de {cor["IA"]}{imc:.2f}{cor["L"]} {cor["I"]}[Sobrepeso].')
elif 30 <= imc < 40:
    print(f'O seu IMC é de {cor["IA"]}{imc:.2f}{cor["L"]} {cor["I"]}[Obesidade].')
else:
    print(f'O seu IMC é de {cor["IA"]}{imc:.2f}{cor["L"]} Obesidade Mórbida.')

print('==' * 20)
print(f'{' ' * 10}10 TERMOS DE UMA PA{' ' * 10}')
print('==' * 20)

# Solicita o usuário a fornecer o primeiro termo e a razão da progressão aritmética
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a sua Razão: '))

# Calcula o décimo termo da progressão aritmética usando a fórmula geral
decimo = primeiro + (10 - 1) * razao

# Loop for para gerar e imprimir os termos da progressão aritmética
# Começa do primeiro termo e vai até o décimo termo, incrementando de acordo com a razão
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' -> ')  # Imprime cada termo seguido de uma seta
print('FIM')  # Imprime 'FIM' após a sequência completa

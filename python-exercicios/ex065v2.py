# Inicializa a variável de resposta e as variáveis de média, quantidade, soma, maior e menor
res = 'S'
media = quant = soma = maior = menor = 0

# Loop continua enquanto a resposta estiver em 'Ss' (ou seja, 'S' ou 's')
while res in 'Ss':
    # Solicita ao usuário para inserir um número
    num = int(input('Digite um número: '))
    
    # Adiciona o número inserido à soma total
    soma += num
    # Incrementa o contador de números inseridos
    quant += 1
    
    # Na primeira iteração, inicializa maior e menor com o primeiro número inserido
    if quant == 1:
        maior = menor = num
    else:
        # Atualiza o maior valor se o número atual for maior que o maior valor anterior
        if num > maior:
            maior = num
        # Atualiza o menor valor se o número atual for menor que o menor valor anterior
        if num < menor:
            menor = num
    
    # Solicita ao usuário se deseja continuar e converte a resposta para maiúscula, considerando apenas o primeiro caractere
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

# Calcula a média dos números inseridos
media = soma / quant

# Exibe a quantidade de números inseridos e a média
print(f'Você digitou {quant} números e a média foi {media}')
# Exibe o maior e o menor valor inseridos
print(f'O maior valor foi {maior} e o menor valor foi {menor}')

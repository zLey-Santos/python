# Inicializa as variáveis: num, cont (contador) e soma
num = cont = soma = 0

# Solicita ao usuário que insira um número, com a condição de que 999 para o loop
num = int(input('Digite um número [Digite 999 para parar]: '))

# Loop continua enquanto o usuário não digitar 999
while num != 999:
    # Adiciona o número inserido à soma total
    soma += num
    # Incrementa o contador de números inseridos
    cont += 1
    # Solicita novamente ao usuário para inserir um número
    num = int(input('Digite um número [Digite 999 para parar]: '))

# Após o loop terminar, exibe a quantidade de números inseridos e a soma total
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')

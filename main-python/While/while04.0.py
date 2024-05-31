# Inicializa as variáveis 'n' e 's' com o valor 0
# 'n' será usada para armazenar os números digitados pelo usuário
# 's' será usada para acumular a soma dos números digitados
n = s = 0

# Inicia um loop infinito
while True:
    # Solicita ao usuário para digitar um número e converte a entrada para um inteiro
    n = int(input('Digite um número: '))
    
    # Verifica se o número digitado é 999
    # Se for, interrompe o loop com o comando 'break'
    if n == 999:
        break
    
    # Adiciona o número digitado à variável 's'
    s += n

# Após o loop terminar, imprime a soma acumulada em 's'
print(f'A soma vale {s}')

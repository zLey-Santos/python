# Inicializa as variáveis 'n', 's' e 'c' com o valor 0
# 'n' será usada para armazenar os números digitados pelo usuário
# 's' será usada para acumular a soma dos números digitados
# 'c' será usada para contar quantos números foram digitados
n = s = c = 0

# Inicia um loop infinito
while True:
    # Solicita ao usuário para digitar um número e converte a entrada para um inteiro
    n = int(input('Digite um número: '))
    
    # Verifica se o número digitado é 999
    # Se for, interrompe o loop com o comando 'break'
    if n == 999:
        break
    
    # Incrementa o contador 'c' em 1 para contar o número de entradas
    c += 1
    
    # Adiciona o número digitado à variável 's'
    s += n

# Após o loop terminar, imprime a quantidade de números digitados e a soma acumulada
print(f'{n} números foram digitados e a soma entre eles é de {s}')

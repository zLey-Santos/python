# Loop infinito para continuar pedindo números ao usuário até que um número negativo seja digitado
while True:
    # Solicita ao usuário para digitar um número e converte a entrada para um inteiro
    n = int(input('Digite um número para ver sua tabuada: '))
    
    # Verifica se o número digitado é negativo
    # Se for, interrompe o loop com o comando 'break'
    if n < 0:
        break  
    
    # Imprime uma linha separadora de 30 caracteres '-' para formatar a saída
    print('-' * 30)

    # Loop que vai de 0 a 10 (inclusive) para gerar a tabuada do número digitado
    for c in range(0, 10 +1):
        # Imprime a multiplicação do número 'n' pelo contador 'c' no formato 'n x c = resultado'
        print(f'{n} x {c} = {n * c}') 
    
    # Imprime outra linha separadora de 30 caracteres '-' para formatar a saída
    print('-' * 30)    

# Imprime 'FIM' quando o loop for interrompido (quando um número negativo for digitado)
print('FIM')    

print('Sequência de Fibonacci.')
print('-'*35)

# Solicita ao usuário o número de termos da sequência de Fibonacci a serem exibidos
n = int(input('Quantos termos você quer mostrar? '))

# Inicializa os dois primeiros termos da sequência de Fibonacci
t1 = 0
t2 = 1
print('-'*35)

# Exibe os dois primeiros termos da sequência
print(f'{t1} -> {t2}', end='')

# Inicia o contador de termos a partir do terceiro termo
cont = 3 

# Continua gerando termos da sequência até alcançar o número desejado pelo usuário
while cont <= n:
    # Calcula o próximo termo da sequência
    t3 = t1 + t2
    # Exibe o próximo termo
    print(f' -> {t3}', end='')
    # Atualiza os valores de t1 e t2 para os próximos cálculos
    t1 = t2
    t2 = t3
    # Incrementa o contador
    cont += 1

print(' -> FIM')

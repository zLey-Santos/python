# Imprime uma linha de separação para o título
print('-' * 30)
# Imprime o título da sequência de Fibonacci
print('Sequência de Fibonacci')
# Imprime outra linha de separação após o título
print('-' * 30)

# Solicita ao usuário o número de termos da sequência a serem mostrados
n = int(input('Quantos termos você quer mostrar? '))

# Inicializa os dois primeiros termos da sequência de Fibonacci
t1, t2 = 0, 1
# Imprime os dois primeiros termos na mesma linha
print(f'{t1} -> {t2}', end=' ')

# Inicializa o contador para acompanhar o número de termos impressos
cont = 3
# Executa um loop para calcular e imprimir os próximos termos da sequência
while cont <= n:
    # Calcula o próximo termo da sequência como a soma dos dois últimos termos
    t3 = t1 + t2
    # Imprime o próximo termo com uma seta (->) antes
    print(f'-> {t3}', end=' ')
    # Atualiza os dois últimos termos para o próximo ciclo do loop
    t1, t2 = t2, t3
    # Incrementa o contador para acompanhar o progresso
    cont += 1

# Após imprimir todos os termos solicitados, imprime "FIM" para indicar o término da sequência
print('FIM')

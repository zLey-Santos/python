# Importa a função randint da biblioteca random para gerar números aleatórios
from random import randint

# Inicializa a variável 'v' com o valor 0, que será usada para contar as vitórias do jogador
v = 0

# Loop infinito para continuar jogando até que o jogador perca
while True:
    # Solicita ao jogador para digitar um número e converte a entrada para um inteiro
    player = int(input('Digite um número: '))
    
    # Gera um número aleatório entre 0 e 10 para o computador
    pc = randint(0, 10)
    
    # Calcula a soma dos números do jogador e do computador
    tot = player + pc
    
    # Inicializa a variável 'type' com um espaço em branco
    type = ' '
    
    # Loop para garantir que o jogador escolha 'P' para par ou 'I' para ímpar
    while type not in 'PI':
        type = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    # Exibe os valores jogados pelo jogador e pelo computador, e o total
    print(f'Você jogou {player} e o computador {pc}. Total de {tot}')
    
    # Verifica se o jogador escolheu par
    if type == 'P':
        # Verifica se o total é par
        if tot % 2 == 0:
            print('Você VENCEU!')
            v += 1  # Incrementa o contador de vitórias
        else:
            print('Você PERDEU!')
            break  # Interrompe o loop se o jogador perder
    # Verifica se o jogador escolheu ímpar
    elif type == 'I':
        # Verifica se o total é ímpar
        if tot % 2 == 1:
            print('Você VENCEU!')
            v += 1  # Incrementa o contador de vitórias
        else:
            print('Você PERDEU!')
            break  # Interrompe o loop se o jogador perder

    # Mensagem indicando que o jogo continua
    print(f'Vamos jogar novamente...')            

# Mensagem final indicando quantas vezes o jogador venceu
print(f'GAME OVER! Você venceu {v} vezes.')

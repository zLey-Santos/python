from random import randint
from time import sleep

# Imprime o cabeçalho do jogo
print(f'{"=" * 12}JOKENPÔ{"=" * 11}')

# Solicita ao usuário que escolha um nickname
name = str(input('Escolha um nickname: '))

# Define as opções de jogadas
items = ('Pedra', 'Papel', 'Tesoura')

# Gera uma jogada aleatória para o computador
computer = randint(0, 2)

# Solicita ao jogador que faça sua jogada
player = int(input(f'{name}, Faça sua jogada: \n [0] para Pedra, \n [1] para Papel, \n [2] para Tesoura:  '))

# Verifica se a escolha do jogador é válida
if player not in [0, 1, 2]:
    print('Jogada inválida! Escolha entre 0, 1 ou 2.')
else:
    # Imprime a contagem regressiva
    print(f'{"-=" * 15}')
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print(f'{"-=" * 15}')

    # Imprime as jogadas escolhidas pelo jogador e pelo computador
    print(f'O computador escolheu: {items[computer]}')
    print(f'O {name} escolheu: {items[player]}')
    print(f'{"-=" * 15}')

    # Verifica quem ganhou o jogo com base nas jogadas
    if computer == player:  # Empate
        print('EMPATE')
    elif computer == 0:  # CPU escolheu Pedra
        if player == 1:
            print('JOGADOR VENCE')
        else:
            print('COMPUTADOR VENCE')
    elif computer == 1:  # CPU escolheu Papel
        if player == 2:
            print('JOGADOR VENCE')
        else:
            print('COMPUTADOR VENCE')
    elif computer == 2:  # CPU escolheu Tesoura
        if player == 0:
            print('JOGADOR VENCE')
        else:
            print('COMPUTADOR VENCE')

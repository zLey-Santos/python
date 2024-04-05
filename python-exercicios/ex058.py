from random import randint
from time import sleep  # Timeout library

# Dictionary of colors for terminal output
colors = {
    'RED'   : '\033[31m',
    'BLUE'  : '\033[34m',
    'PURPLE': '\033[35m',
    'YELLOW': '\033[33m',
    'GREEN' : '\033[32m',
    'CYAN'  : '\033[36m',
    'RESET' : '\033[m'
}

# Initial presentation
print('-=-' * 22)
print(f"{colors['PURPLE']} Eu sou seu computador...{colors['RESET']} Acabei de pensar em um número entre {colors['PURPLE']}0 e 10{colors['RESET']}.\n"
      f"{colors['BLUE']} Será que você consegue adivinhar qual é? {colors['RESET']}")
print('-=-' * 22)

# Generate a random number between 0 and 10
num_cpu = randint(0, 10)
guessed = False
attempts = 0

# Loop until the player guesses the number
while not guessed:
    # Player's guess
    guess = int(input('Qual é o seu palpite: '))
    attempts += 1

    if guess == num_cpu:
        # If the guess is correct
        print(f"{colors['GREEN']} Parabéns! Você acertou o número {colors['PURPLE']}[{num_cpu}]{colors['RESET']}"
              f"{colors['GREEN']} na sua {colors['PURPLE']}{attempts}ª{colors['RESET']} tentativa.{colors['RESET']}")
        guessed = True
    else:
        # If the guess is incorrect
        if guess > num_cpu:
            print(f"{colors['RED']}Seu palpite está muito alto!{colors['RESET']}")
        elif guess < num_cpu:
            print(f"{colors['YELLOW']}Seu palpite está muito baixo!{colors['RESET']}")
        print(f"{colors['CYAN']}Tente novamente...{colors['RESET']}")
        sleep(1)  # Pause time before the next attempt

print(f"\n{'==' * 22}")
 
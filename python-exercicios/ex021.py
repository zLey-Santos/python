import pygame
# Inicialização do pygame
pygame.init()
print('***_-Grego_Morena-_***')
print(f'-_-_-_-_-PLAY-_-_-_-_-')
# Carregar o arquivo de música
pygame.mixer.music.load('ex021.mp3')
# Reproduzir a música
pygame.mixer.music.play()
input()
# Aguardar o término da reprodução da música
pygame.event.wait()

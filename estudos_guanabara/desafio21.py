import pygame
pygame.init() #inicia a biblioteca pygame
pygame.mixer.music.load('risada.mp3') #lê o arquivo mp3
pygame.mixer.music.play(loops=0) #da play na musica que foi lida
input() #necessario para iniciar o mixer
pygame.event.wait() #espera o evento acabar para encerrar o programa

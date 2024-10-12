import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load('mp3-sound/tanjiro01.mp3')
pygame.mixer.music.play()

print("Digite 'pause' para interromper a música.")

while pygame.mixer.music.get_busy():
    command = input("Escreva o comando: ").lower()
    if command == 'pause':
        pygame.mixer.music.stop()
        print("Música foi parada.")
        break
    time.sleep(1)
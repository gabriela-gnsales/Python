# Tocando um MP3

import pygame

pygame.init()
pygame.mixer.music.load('dua_lipa_idgaf.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

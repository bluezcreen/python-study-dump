import pygame

#gaster simulator
pygame.mixer.init()
pygame.mixer.music.load("ANOTHER HIM.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
	pass
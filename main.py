import pygame
from os import path
import config

WIDTH = 800
HEIGHT = 450

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

img = pygame.image.load('карта.png')

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    window.blit(img, (0,0))

    pygame.display.update()
    clock.tick()

pygame.quit()
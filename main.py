import pygame.key
from pygame.sprite import Sprite
from pygame import Surface, image, transform
import random
import config
running = True


screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
clock = pygame.time.Clock()

image = image.load('assets/karta.png')
rect = image.get_rect()

while running:
    clock.tick(config.FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
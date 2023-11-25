import pygame
import Sprites
import config

WIDTH = 800
HEIGHT = 450

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

img = pygame.image.load('assets/karta.png')
print(img.get_size())
img = pygame.transform.scale(img, (800, 450))

play = True
while play:
    clock.tick(config.FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    window.blit(img, (0,0))

    pygame.display.update()
    clock.tick()

pygame.quit()


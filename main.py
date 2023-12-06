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

countries = pygame.sprite.Group()

countries_list = [
    Sprites.Africa(),Sprites.Mongolia(),Sprites.Kazakhstan(),Sprites.Scandinavia(),Sprites.China(),Sprites.Europe(),
    Sprites.North_America(),Sprites.South_America(),Sprites.Australia(),Sprites.Greenland(),Sprites.Russia(),
    Sprites.Xynta()
]

for i in countries_list:
    countries.add(i)

play = True
while play:
    clock.tick(config.FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    countries.update()

    window.blit(img, (0,0))
    for country in countries.sprites():
        country.draw(window)
    pygame.display.update()

pygame.quit()
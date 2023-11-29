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
countries.add(Sprites.African_countries())
countries.add(Sprites.Kazakhstan())
countries.add(Sprites.Scandinavia())
countries.add(Sprites.China())
countries.add(Sprites.Europe())
countries.add(Sprites.North_America())
play = True
while play:
    clock.tick(config.FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    window.blit(img, (-10,-5))
    for country in countries.sprites():
        country.draw(window)
    pygame.display.update()

pygame.quit()


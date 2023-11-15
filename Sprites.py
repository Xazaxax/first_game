import random

from pygame.sprite import Sprite
from pygame import Surface
import config


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = Surface((50, 50))
        self.image.fill(config.COLOR['BLUE'])
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH / 2, config.HEIGHT / 2)

        self.speed_x = 30
        self.speed_y = 20

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x > config.WIDTH - self.rect.width or self.rect.x < 0:
            self.speed_x = -self.speed_x
            self.speed_x *= 0.7

        if self.rect.y > config.HEIGHT - self.rect.height or self.rect.y < 0:
            self.speed_y = -self.speed_y
            self.speed_y *= 0.7
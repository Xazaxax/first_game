import random
import pygame as pg
from pygame.sprite import Sprite
from pygame import Surface
import config
import pygame


class Country:
    def __init__(self, name: str,people,sicked,koef_e,polygon):
        self.name = name
        self.people = people
        self.sicked = sicked
        self.koef_e = koef_e
        self.polygon = polygon

    def update(self):
        self.sicked += 2

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(
            screen,
            pygame.Color(255, 255, 255),
            self.polygon
        )

        percent_sicked = int(0.0456 * 255)

        pygame.draw.polygon(
            screen,
            pygame.Color(255, 0, 0, percent_sicked),
            self.polygon
        )

class Kazakhstan(Country):
    def __init__(self):
        super().__init__("Казахстан",19000000,0,0.6,[
            [565,164],[570,152],[550,146],[518,152],[489,164],[518,170],[530,176],[541,176]
        ])

class Scandinavia(Country):
    def __init__(self):
        super().__init__("Скандинавия", 22000000, 0, 0.7, [
            [407,91],[397,121],[385,125],[374,116],[379,98],[407,71],[436,64],[462,80],[454,85],
            [440,82],[443,102],[414,110],[417,91],[407,91],[397,121]
        ])

class African_countries(Country):
    def __init__(self):
        super().__init__("Африканские страны", 1429000000, 0, 0.4, [
            [579,228],[555,267],[541,239],[507,220],[485,251],[450,220],[460,196],[507,190],
            [542,196],[570,220]
        ])

class China(Country):
    def __init__(self):
        super().__init__("Китай",1412000000, 0, 0.85,[
            [555,196],[565,210],[602,214],[633,234],[667,220],[658,190],[695,175],[685,152],[658,164],
            [633,179],[596,170],[560,179]
        ])

class Europe(Country):
    def __init__(self):
        super().__init__("Европа",746400000, 0, 0.8,[
            [450,164],[418,190],[379,170],[348,190],[337,179],[374,136],[407,136],[418,121]
        ])

class North_America(Country):
    def __init__(self):
        super().__init__("Северная Америка", 579000000, 0, 0.75, [
            [62,159],[35,179],[49,203],[99,251],[139,261],[129,239],[111,246],[104,220],[139,210],[163,190]
            ,[169,175],[127,176],[95,159]
        ])

class Kanada(Country):
    def __init__(self):
        super().__init__("Канада",40000000,0,0.6,[
            [62,159],[129,159],[172,170],[209,146],[189,115],[163,106],[145,146],[111,115],[129,90]
            ,[119,71],[62,82],[21,115],[35,152]
        ])
#       def update(self):
#          if self.population/2 < self.infected:
#              self.infected -= 5


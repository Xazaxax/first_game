import random
import pygame as pg
from pygame.sprite import Sprite
from pygame import Surface
import config


class Country(Sprite):
    def __init__(self, k_infected , population , infected):
        self.k_infected = k_infected
        self.population = population
        self.infected = infected
        russia = {'k_infected':(0.9), 'population':(145478097), 'infected':(0)}
        germany ={'k_infected':(0.7)}
        usa = {'k_infected':(0.85)}
        kanada = {'k_infected':(0.75)}
        australia = {'k_infected':(0.6)}
        nigeria = {'k_infected':(0.4)}
        china = {'k_infected':(0.9)}
        brazilia = {'k_infected':(0.7)}


        def update(self):
            if self.population/2 < self.infected:
                self.infected -= 5


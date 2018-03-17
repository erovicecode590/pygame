import pygame as pg

from settings import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

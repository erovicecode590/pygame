import pygame as pg

from settings import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)*TILESIZE
        self.vel = vec(0, 0)

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.vel += vec(PLAYER_SPEED, 0)
        if keys[pg.K_LEFT]:
            self.vel = vec(-PLAYER_SPEED, 0)
        if keys[pg.K_UP]:
            self.vel += vec(0, -PLAYER_SPEED)
        if keys[pg.K_DOWN]:
            self.vel = vec(0, PLAYER_SPEED)

    def update(self):
        self.get_keys()
        self.rect.center = self.pos
        self.pos += self.vel*self.game.dt

#=============================================================
# Description   :Sprite classes are created and properties
#                such as movement and collisions are defined.
#=============================================================

# Import pygame module to access pygame functions.
import pygame as pg

# Import properties from settings file.
from settings import *

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.set_colorkey(BLACK)
        image.blit(self.spritesheet, (0,0), (x, y, width, height))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # Define initial properties for sprite when created.
        self.groups = game.all_sprites # Defines group(s) sprite belongs to.
        # Line necessary for sprite to be initialized in pygame.
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game # Allows sprite to reference self in game object.
        self.image = self.game.characters.get_image(623, 1013, 194, 218)
        self.rect = self.image.get_rect() # Defines rect to manage sprite placement.
        self.pos = VEC(x, y)*TILESIZE # Sprite placement based on location called to.
        self.vel = VEC(0, 0)

    def get_keys(self):
        # Method for obtaining keys pressed by player/user to move sprite.
        self.vel = VEC(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.vel += VEC(PLAYER_SPEED, 0)
        if keys[pg.K_LEFT]:
            self.vel = VEC(-PLAYER_SPEED, 0)
        if keys[pg.K_UP]:
            self.vel += VEC(0, -PLAYER_SPEED)
        if keys[pg.K_DOWN]:
            self.vel += VEC(0, PLAYER_SPEED)

    def update(self):
        # Method for updated changes/properties of sprite.
        self.get_keys()
        self.rect.center = self.pos
        self.pos += self.vel*self.game.dt

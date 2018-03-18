#==================================================
#description    :Properties for sprites, game and
#                tile map are defined here.
#==================================================
# Import module to run pygame.
import pygame as pg

# Window width and height.
WIDTH = 1032
HEIGHT = 786
DISPLAY = (WIDTH, HEIGHT)

FPS = 60 # Define frames per second.

# Colors are defined with respect to RGB (Red, Green, Blue).
#                  R    G    B
BLACK           = (0,   0,   0)
WHITE           = (255, 255, 255)
LIGHTGREY       = (150, 150, 150)
DARKGREY        = (50,  50,  50)
RED             = (255,  0,  0)
GREEN           = (0,  255,  0)
BLUE            = (0,  0,  255)

# tile size to adjust pixel size to.
TILESIZE = 32

# Player Properties.
PLAYER_SPEED = 150

#Spritesheets used
CHARACTER_SPRITESHEET = "spritesheet_characters.png"

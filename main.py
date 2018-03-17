import pygame as pg
import sys

from os import path
from settings import *
from sprites import *

class Game():
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.running = True
        self.screen = pg.display.set_mode(DISPLAY)

    def new_game(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, 5, 5)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
<<<<<<< HEAD
        self.screen.fill(DARKGREY)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def load_data(self):
        pass

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
=======
        self.screen.fill(BLACK)
>>>>>>> bb6258e8bc901df9e2e20f1b268075a49e3e4503

g = Game()
g.show_start_screen()
while g.running:
    g.new_game()
    g.run()
<<<<<<< HEAD
    g.show_go_screen()
pg.quit()
=======

pygame.quit()
>>>>>>> bb6258e8bc901df9e2e20f1b268075a49e3e4503
sys.exit()

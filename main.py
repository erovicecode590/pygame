#============================================================
#title              :tile based game script
#description        :template for a pygame script
#author             :Alan Ramirez
#date               :date
#usage              :python main.py
#notes              :
#python_version     :3.6.2
#============================================================

# Import pygame module needed to run script
import pygame as pg
import sys

# Import path to join files from other directories.
from os import path

# Import everything from other py files in directory for use.
from settings import *
from sprites import *

# Create a game object and define methods to call.
class Game():
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.running = True
        self.screen = pg.display.set_mode(DISPLAY)

    def new_game(self):
        # Initialize setup of sprites when a new game is started.
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, 5, 5)

    def run(self):
        # Method which calls other methods while game loop is active.
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000 # time change in the game.
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Keeps track of player/user input from keys/mouse clicks.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        # Updates all sprite movement and changes within groups.
        self.all_sprites.update()

    def draw(self):
        # Redraw changes on to the screen.
        self.screen.fill(DARKGREY) # Background color
        self.all_sprites.draw(self.screen) # Draw all sprites within group on to screen.
        pg.display.flip() # Update everything on to the screen.

    def load_data(self):
        # Load data from py files and other files.
        pass
        game_folder = path.dirname(__file__)
        img_dir = path.join(game_folder,'images')

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

def start_game():
    # Call game object and methods to run script.
    g = Game()
    g.show_start_screen()
    while g.running:
        g.new_game()
        g.run()
        g.show_go_screen()
    pg.quit()
    sys.exit()

if __name__ == '__main__':
    start_game()

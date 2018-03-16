import pygame
import sys

from settings import *

class Game():
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode(DISPLAY)

    def run(self):
        self.events()
        self.update()
        self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pygame.display.update()

    def draw(self):
        self.screen.fill(BLACK)

g = Game()
while g.running:
    g.run()

pygame.quit(
sys.exit()
)

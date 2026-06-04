# pylint: disable=import-error
import pygame

from gameObject.player import Player

# transformar platform em objeto 
class GameWorld:

    def __init__(self):

        self.player = Player(100, 300)

        self.entities = [self.player]

    def update(self, dt, keys):

        for entity in self.entities:
            entity.update(dt, keys, platforms)

    def render(self, screen):
        self.player.draw(screen)

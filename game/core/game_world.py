# pylint: disable=import-error
import pygame

from player import Player


class GameWorld:

    def __init__(self):

        self.player = Player(100, 300)

        self.entities = [self.player]

        self.ground = pygame.Rect(0, 500, 800, 100)

    def update(self, dt, keys):

        for entity in self.entities:
            entity.update(dt, keys, self.ground)

    def render(self, screen):

        pygame.draw.rect(screen, (100, 255, 100), self.ground)

        for entity in self.entities:
            entity.draw(screen)

# pylint: disable=import-error
import pygame

from gameObject.player import Player


class GameWorld:

    def __init__(self):

        self.player = Player(100, 300)

        self.entities = [self.player]

        self.platforms = [
            pygame.Rect(0, 500, 800, 100),   # chão
            pygame.Rect(300, 400, 200, 20),  # plataforma 1
            pygame.Rect(100, 300, 150, 20),  # plataforma 2
        ]

    def update(self, dt, keys):

        for entity in self.entities:
            entity.update(dt, keys, self.platforms)

    def render(self, screen):

        for platform in self.platforms:
            pygame.draw.rect(screen, (100, 255, 100), platform)

        self.player.draw(screen)

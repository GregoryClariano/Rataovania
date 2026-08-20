import pygame

from gameObject.player import Player
from gameObject.platform import Platform


class GameWorld:

    def __init__(self):

        self.player = Player(100, 300)

        platform_sprite = pygame.image.load("sprites/platform.png").convert_alpha()


        self.platforms = [

            Platform(
                pygame.Vector2(0, 500),
                platform_sprite,
                pygame.Rect(0, 500, 800, 100)
            ),

            Platform(
                pygame.Vector2(300, 400),
                platform_sprite,
                pygame.Rect(300, 400, 200, 20)
            ),

            Platform(
                pygame.Vector2(100, 300),
                platform_sprite,
                pygame.Rect(100, 300, 150, 20)
            ),

            Platform(
                pygame.Vector2(600, 350),
                platform_sprite,
                pygame.Rect(600, 350, 150, 20)
            )
        ]

        for platform in self.platforms:
            platform.update_hitbox()
                
        self.entities = [
            self.player
        ]

    def update(self, dt, keys):

        for entity in self.entities:
            entity.update(dt, keys, self.platforms)

    def render(self, screen):

        for platform in self.platforms:
            platform.draw(screen)

        self.player.draw(screen)

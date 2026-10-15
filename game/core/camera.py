import pygame


class Camera:
    def __init__(self, screen_width, screen_height):
        self.offset = pygame.Vector2(0, 0)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, target):
        self.offset.x = (
            target.rect.centerx - self.screen_width / 2
        )
        self.offset.y = (
            target.rect.centery - self.screen_height / 2
        )

    def apply(self, position):
        return pygame.Vector2(position) - self.offset

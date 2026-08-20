import pygame

class StaticObject:

    def __init__(self, position, sprite, hitbox):

        self.position = pygame.Vector2(position)
        self.sprite = sprite
        self.hitbox = hitbox

    def update_hitbox(self):

        self.hitbox.topleft = (
            int(self.position.x),
            int(self.position.y)
        )

    def draw(self, screen):

        screen.blit(self.sprite, self.position)
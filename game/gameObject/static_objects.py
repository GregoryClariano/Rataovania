import pygame

from core.physics import Rigidbody

class StaticObject:
    def __init__(self, possition, sprite):
        self.possition = pygame.Vector2(possition)
        self.sprite = sprite
        
    def draw(self, screen):
        screen.blit(self.sprite, self.possition)
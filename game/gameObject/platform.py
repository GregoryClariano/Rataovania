import pygame

from core.physics import Rigidbody

class Platform(StaticObject):
    def __init__(self, rect):
        self.rect = rect
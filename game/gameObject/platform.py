import pygame

from static_objects import StaticObject

class Platform(StaticObject):
    def __init__(self, rect):
        self.rect = rect
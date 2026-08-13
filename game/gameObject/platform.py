import pygame

from static_objects import StaticObject

class Platform(StaticObject):
    def __init__(self, positioin, rect):
        self.rect = rect